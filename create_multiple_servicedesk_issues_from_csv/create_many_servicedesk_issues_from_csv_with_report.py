import atexit
import csv
import hashlib
import json
import os
from datetime import datetime

from assignable_users.get_assignable_users import get_all_assignable_users_email
from auth_and_headers import jira_auth_and_headers
from get_to_kow_your_instance.get_to_know_your_servicedesk import get_my_instance_details
from create_servicedesk_issue.servicedesk_create_issue_on_behalf_of_someone_else import create_issue

auth, headers, base_url = jira_auth_and_headers()
my_instance_servicedesks = get_my_instance_details()
# Input to the below NEEDS to be a non-servicedesk Jira project in the SAME instance
assignable_users = get_all_assignable_users_email("D1")
init_ = {}
initiative_name_ = ""


@atexit.register
def store_report():
    with open(f'reports/{initiative_name_}.json', 'w') as outfile:
        json.dump(init_, outfile)


def create_servicedesk_issues(csv_file_, init_name_):
    global init_
    global initiative_name_
    initiative_name_ = init_name_
    f_name = f"reports/{initiative_name_}.json"
    if os.path.exists(f_name):
        with open(f'reports/{initiative_name_}.json', 'r+') as initiative_:
            init_ = json.load(initiative_)
    else:
        init_['created'] = []
        init_['issues'] = {}
    with open(csv_file_) as infile:
        reader = csv.reader(infile, delimiter=",")
        # Skip the header
        next(reader, None)
        # For each row
        for row in reader:
            row_tuple = tuple(row)
            hash_ = hashlib.md5()
            for entry in row_tuple:
                hash_.update(entry.encode())
            row_hash = hash_.hexdigest()
            # Are we doing work or not?
            if row_hash not in init_['created']:
                date_ = str(datetime.utcnow())
                service_desk_id = my_instance_servicedesks.get("service_desks", {}).get(row[1], None)
                request_type_id = my_instance_servicedesks.get("request_types", {}).get(service_desk_id, {}).get(row[2],
                                                                                                                 None)
                raise_on_behalf_of_id = assignable_users.get(row[0], None)
                res = create_issue(service_desk_id_=service_desk_id,
                                   request_type_id_=request_type_id,
                                   summary_=row[3],
                                   description_=row[4],
                                   raise_on_behalf_of_=raise_on_behalf_of_id)
                json_res = json.loads(res.text)
                issue_key = json_res['issueKey']
                init_['issues'][f'{issue_key}'] = {
                    "date_opened": date_,
                    "raised on behalf of": row[0],
                    "hash": f"{row_hash}",
                    "status_category": "new",
                    "url": f"{base_url}browse/{issue_key}",
                    "reminder": []
                }
                init_['created'].append(row_hash)


if __name__ == "__main__":
    csv_file = "input/emails_all_vars.csv"
    initiative_name = "my_servicedesk_automation"
    create_servicedesk_issues(csv_file, initiative_name)
