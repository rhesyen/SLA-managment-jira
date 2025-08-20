from __future__ import annotations

from jira import JIRA

# Authentication Methods
jira = JIRA(
    # Do uzupełnienia:
    # server="https://moj_serwer.net",
    # basic_auth=("mail@firma.com", "JIRA_TOKEN"),  # Jira Cloud: a username/token tuple
)

all_issues = jira.search_issues(
    'project = "Nazwa projektu" AND createdDate >= startOfMonth(-2) AND createdDate <= endOfMonth(0) AND status IN (Zrealizowane, Zamknięte) ORDER BY created DESC, key ASC')
rows = []
for issue in all_issues:
    fields = {}
    for field_name in issue.raw['fields']:
        fields[field_name] = issue.raw['fields'][field_name]
    requestType = fields.get('customfield_10010').get('requestType').get('name')
    reaction = fields.get('customfield_10055').get('completedCycles')[-1].get('elapsedTime')
    reactionColor = "unset" if fields.get('customfield_10055').get('completedCycles')[-1].get('remainingTime').get(
        "millis") >= 0 else "red"

    resolve = fields.get('customfield_10056').get('ongoingCycle')
    if not resolve:
        resolve = fields.get('customfield_10056').get('completedCycles')[-1]

    resolveColor = "unset" if resolve.get('remainingTime').get("millis") >= 0 else (
        "red" if resolve.get('remainingTime').get('friendly') != "0 min" else "unset")
    resolve = resolve.get('elapsedTime')

    reporter = fields.get('reporter')
    status = fields.get('status').get('name')
    statusColor = fields.get('status').get('statusCategory').get('colorName')
    row_template = f"""
    <tr>
        <td><a href="https://moj_serwer.net/servicedesk/customer/portal/153/group/161/browse/{issue.key}" target="_blank">{issue.key}</a></td>
        <td>{requestType}</td>
        <td>{fields.get('summary')}</td>
        <td>{fields.get('created').replace('+0200', '')}</td>
        <td>{fields.get('updated').replace('+0200', '')}</td>
        <td style="color: {reactionColor}">{reaction.get('friendly')}</td>
        <td style="color: {resolveColor}">{resolve.get('friendly')}</td>
        <td style="color: {statusColor}">{status}</td>
        <td>{reporter.get('displayName')} ({reporter.get('emailAddress')})</td>
    </tr>
    """

    rows.append(row_template)
rows = ''.join(rows)


open("raport.html", "w+", encoding="utf-8").write("""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Raport SLA</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0d1117;
            color: #c9d1d9;
            margin: 0;
            padding: 20px;
        }
        a,a:link,
        a:visited,
        a:hover, a:focus,
        a:active         { color: #c9d1d9; text-decoration:none }

        .header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
        }
        .header img {
            height: 50px;
            margin-right: 20px;
        }
        h1 {
            color: #58a6ff;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            text-align: left;
            border-bottom: 1px solid #30363d;
        }
        th {
            background-color: #161b22;
            color: #58a6ff;
        }
        tr:nth-child(even) {
            background-color: #161b22;
        }
    </style>
</head>
<body>

<div class="header">
    <h1>Raport SLA</h1>
</div>

<table>
    <thead>
        <tr>
            <th>Klucz</th>
            <th>Typ zgłoszenia</th>
            <th>Podsumowanie</th>
            <th>Utworzono</th>
            <th>Zaktualizowano</th>
            <th>Czas reakcji</th>
            <th>Czas naprawy</th>
            <th>Status</th>
            <th>Osoba zgłaszająca</th>
        </tr>
    </thead>
    <tbody>
        """ + rows + """
    </tbody>
</table>

</body>
</html>
"""
)