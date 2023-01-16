import requests
from auth_and_headers import jira_auth_and_headers
import json


def get_all_servicedesks():
    """Gets all request types for all service desks

              Returns:
                  Json Object: returns all request types with service desk and request type attributes expanded

           """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}rest/servicedeskapi/servicedesk?expand=serviceDesk,requestType"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    json_res = json.loads(response.text)

    return json_res


def get_servicedesk_issue(this_issue_key):
    """Gets all fields set and vacant for the epic or story queried

        Parameters:
            this_issue_key (string): issue identifier eg: D1-1
        Returns:
            Json Object: Object has all fields available set and vacant for the story/epic

   """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}/rest/servicedeskapi/request/{this_issue_key}"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    text_contents = json.loads(response.text)
    return text_contents


def get_all_request_types():
    """Gets all request types for all service desks

              Returns:
                  Json Object: returns all request types with service desk and request type attributes expanded

           """
    auth, headers, base_url = jira_auth_and_headers()
    url = f"{base_url}rest/servicedeskapi/requesttype?expand=serviceDesk,requestType"

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )
    json_res = json.loads(response.text)

    return json_res


if __name__ == "__main__":

    issue = get_all_servicedesks()
    print(json.dumps(issue, indent=4))

    # issue_key = "ST-4"
    # issue = get_servicedesk_issue(issue_key)
    # print(json.dumps(issue, indent=4))

    # field_configurations = get_all_request_types()
    # print(json.dumps(field_configurations, indent=4))
