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
url2 = f"{base_url}/rest/api/3/issue/{issueIdOrKey}?expand=names"

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url2,
   headers=headers,
   auth=auth
)

data = response.json()

# print("Nazwy pól niestandardowych w zgłoszeniu:")
# for field_id, field_name in data.get("names", {}).items():
#     if field_id.startswith("customfield_"):
#         print(f"{field_id} => {field_name}")

# print("Informacje i czasy SLA dla Issue o danej nazwie:")
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))