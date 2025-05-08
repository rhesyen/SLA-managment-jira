# SLA-managment-jira
Simple script for SLA data analysis from Jira (internal use)
## Python libraries
* 'requests' library: [http://docs.python-requests.org]
* 'dotenv' library
* 'os' library

## Build-in safety
Requires creating a personal `.env` file in the same folder, with following variables:
* `JIRA_EMAIL=your_atlassian_email`
* `JIRA_BASE_URL=https://company.atlassian.net`
* `JIRA_ISSUE=#####-###` - issueIdOrKey provided in upperletters
* `JIRA_TOKEN=ABC...DEF` - combination of letters from created API token, connected to provided account [https://id.atlassian.com/manage-profile/security/api-tokens]

More details in documentation: [https://developer.atlassian.com/server/jira-servicedesk/rest/v1006/api-group-customer-request/#api-servicedeskapi-request-issueidorkey-sla-get]
