import csv

from assignable_users.get_assignable_users import get_all_assignable_users_email
from auth_and_headers import jira_auth_and_headers
from get_to_kow_your_instance.get_to_know_your_servicedesk import get_my_instance_details
from create_servicedesk_issue.servicedesk_create_issue_on_behalf_of_someone_else import create_issue

auth, headers, base_url = jira_auth_and_headers()
my_instance_servicedesks = get_my_instance_details()
# Input to the below NEEDS to be a non-servicedesk Jira project in the SAME instance
assignable_users = get_all_assignable_users_email("D1")


def create_servicedesk_issues(csv_file_, service_desk_name_, request_type_, summary_, description_):
    with open(csv_file_) as infile:
        reader = csv.reader(infile, delimiter=",")
        # Skip the header
        next(reader, None)
        # For each row
        for row in reader:
            service_desk_id = my_instance_servicedesks.get("service_desks", {}).get(service_desk_name_, None)
            request_type_id = my_instance_servicedesks.get("request_types", {}).get(service_desk_id, {}).get(request_type_,
                                                                                                         None)
            raise_on_behalf_of_id = assignable_users.get(row[0], None)
            create_issue(service_desk_id, request_type_id, summary_, description_, raise_on_behalf_of_id)


if __name__ == "__main__":
    csv_file = "input/emails.csv"
    # service_desk_name, request_type, summary and description may be in the CSV
    service_desk_name = "DR_SD"
    request_type = "Set up VPN to the office"
    summary = "DR human-readable to codes"
    description = "I need a new *mouse* for my Mac"
    create_servicedesk_issues(csv_file, service_desk_name, request_type, summary, description)
