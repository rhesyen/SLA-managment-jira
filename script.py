# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import json

load_dotenv()

base_url = os.getenv("JIRA_BASE_URL")
issueIdOrKey = os.getenv("JIRA_ISSUE")
email = os.getenv("JIRA_EMAIL")
api_token = os.getenv("JIRA_TOKEN")

url = f"{base_url}/rest/servicedeskapi/request/{issueIdOrKey}/sla/"

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))