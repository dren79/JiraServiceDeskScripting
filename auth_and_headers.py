import requests
from dotenv import load_dotenv
import os

load_dotenv()


def jira_auth_and_headers():
    """Gets all fields set and vacant for the epic or story queried

       Returns:
           auth: (HTTPBasicAuth object) for the Jira Cloud instance
           headers: (json object) contains required headers for all requests
           url: (String) the base URL for the instance

    """
    auth = requests.auth.HTTPBasicAuth(os.environ.get("JIRA_EMAIL_K"), os.environ.get("API_KEY_K"))

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "X-ExperimentalApi": "opt-in"
    }

    url = os.environ.get("BASE_URL_K")

    return auth, headers, url
