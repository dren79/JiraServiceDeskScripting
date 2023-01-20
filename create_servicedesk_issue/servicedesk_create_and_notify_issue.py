import requests
import json

from assignable_users.get_assignable_users import get_all_assignable_users_email
from auth_and_headers import jira_auth_and_headers
from get_to_kow_your_instance.get_to_know_your_servicedesk import get_my_instance_details


def create_issue(service_desk_id_, request_type_id_, summary_, description_, also_notify_=None):
    """Creates a story under an epic

      Parameters:
            :param assignee_: ID of the user we want to assign the issue to
            :param service_desk_id_: The id of the service desk, use the get to know your instance json to convert from name to id
            :param request_type_id_: The id of the request type, use the get to know your instance json to convert from name to id
            :param summary_: Text summary for the issue
            :param description_: Text description of the issue

      Returns:
        response object: This will have the response code and in the text will have the key of the created issue.
        

     """
    auth, headers, base_url = jira_auth_and_headers()

    url = f'{base_url}/rest/servicedeskapi/request?expand="participant","status","sla","requestType","serviceDesk","attachment","action","comment"'

    payload_json = {
        "serviceDeskId": service_desk_id_,
        "requestTypeId": request_type_id_,
        "requestFieldValues": {
            "summary": summary_,
            "description": description_
        }
    }
    if also_notify_ is not None:
        payload_json["requestParticipants"] = []
        payload_json["requestParticipants"].append(also_notify_)

    payload = json.dumps(payload_json)

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )
    return response


if __name__ == "__main__":
    # converting human-readable to the id's service desk needs
    my_instance_servicedesks = get_my_instance_details()
    service_desk_name = "DR_SD"
    request_type = "Set up VPN to the office"
    serviceDeskId = my_instance_servicedesks.get("service_desks", {}).get(service_desk_name, None)
    requestTypeId = my_instance_servicedesks.get("request_types", {}).get(serviceDeskId, {}).get(request_type, None)
    # adding the text attributes
    summary = "DR human-readable to codes"
    description = "I need a new *mouse* for my Mac"
    # convert assignee email to id
    also_notify_email = "devfestireland@gmail.com"
    # the project ID below needs to be a non-service desk standard Jira project in the same instance of Jira
    also_notify = get_all_assignable_users_email("D1").get(also_notify_email, None)
    res = create_issue(serviceDeskId, requestTypeId, summary, description, also_notify)
    if res.status_code == 400:
        json_res = json.loads(res.text)
        print(json_res['errorMessages'])
    else:
        json_res = json.loads(res.text)
        issue_key = json_res['issueKey']
        print(f"New Issue Key: {issue_key}")
