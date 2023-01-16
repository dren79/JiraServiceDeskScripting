import requests
import json
from auth_and_headers import jira_auth_and_headers


def create_issue(service_desk_id_, request_type_id_, summary_, description_):
    """Creates a story under an epic

      Parameters:
            :param service_desk_id_: The id of the service desk, use the get to know your instance json to convert from name to id
            :param request_type_id_: The id of the request type, use the get to know your instance json to convert from name to id
            :param summary_: Text summary for the issue
            :param description_: Text description of the issue

      Returns:
        response object: This will have the response code and in the text will have the key of the created issue.
        

     """
    auth, headers, base_url = jira_auth_and_headers()

    url = f'{base_url}/rest/servicedeskapi/request?expand="participant","status","sla","requestType","serviceDesk","attachment","action","comment"'

    payload = json.dumps({
        "serviceDeskId": service_desk_id_,
        "requestTypeId": request_type_id_,
        "requestFieldValues": {
            "summary": summary_,
            "description": description_
        }
    })

    response = requests.request(
       "POST",
       url,
       data=payload,
       headers=headers,
       auth=auth
    )
    return response


if __name__ == "__main__":
    serviceDeskId = "2"
    requestTypeId = "22"
    summary = "DR Request JSD help via REST"
    description = "I need a new *mouse* for my Mac"
    res = create_issue(serviceDeskId, requestTypeId, summary, description)
    if res.status_code == 400:
        json_res = json.loads(res.text)
        print(json_res['errorMessages'])
    else:
        json_res = json.loads(res.text)
        issue_key = json_res['issueId']
        print(f"New Issue Key: {issue_key}")
