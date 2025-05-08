# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import os

import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import json

load_dotenv()

base_url = os.getenv("JIRA_BASE_URL")
issueIdOrKey = "#######"
email = os.getenv("JIRA_EMAIL")
api_token = os.getenv("JIRA_TOKEN")

url2 = f"{base_url}/rest/api/3/issue/{issueIdOrKey}"

auth = HTTPBasicAuth(email, api_token)

headers = {
  "Accept": "application/json"
}

params = {
    "maxResults" : 10
}

response = requests.request(
   "GET",
   url2,
   headers=headers,
   auth=auth
)

if response.status_code != 200:
    print(f"Błąd: {response.status_code} - {response.text}")
    exit()

data = response.json()

print(data)