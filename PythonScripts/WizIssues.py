# Python 3.6+
# This Python script iterates through all issues and prints out by status and severity


import os
import http.client
import json
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport
import requests
import csv


client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

# The GraphQL query that defines which data you wish to fetch.
query = gql("""
  query IssuesTableExport($filterBy: IssueFilters, $orderBy: IssueOrder, $limit: Int!) {
    export: issues(filterBy: $filterBy, orderBy: $orderBy) {
      exportUrl(limit: $limit)
    }
  }
""")

# The variables sent along with the above query
variables = {
  'filterBy': {
    'status': [
      'OPEN',
      'IN_PROGRESS',
      'REJECTED',
      'RESOLVED'
    ],
    'relatedEntity': {}
  },
  'orderBy': {
    'field': 'SEVERITY',
    'direction': 'DESC'
  },
  'limit': 5000
}

def query_wiz_api(access_token, query, variables):
  """Qeury WIZ API for the given query data schema"""
  transport = AIOHTTPTransport(
    url="https://api.eu1.demo.wiz.io/graphql",
    headers={'Authorization': 'Bearer ' + access_token}
  )
  client = Client(transport=transport, fetch_schema_from_transport=True, execute_timeout=55)

  # Fetch the query!
  result = client.execute(query, variable_values=variables)
  return result

def request_wiz_api_token(client_id, client_secret):
  """Retrieve an OAuth access token to be used against Wiz API"""
  headers = {
    "content-type": "application/x-www-form-urlencoded"
  }
  payload = f"grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}&audience=beyond-api"

  conn = http.client.HTTPSConnection("auth0.demo.wiz.io")
  conn.request("POST", f"/oauth/token", payload, headers)
  res = conn.getresponse()
  token_str = res.read().decode("utf-8")

  if "access_token" in json.loads(token_str):
    return json.loads(token_str)["access_token"]
  else:
    print("Failed requesting API token. Error:")
    print(json.loads(token_str))
    exit()

token = request_wiz_api_token(client_id, client_secret)
result = query_wiz_api(token, query, variables)

urlresult = result['export']['exportUrl'] # your data is here!

#print(urlresult)
r = requests.get(urlresult, allow_redirects=True)
open('critical.csv', 'wb').write(r.content)


with open('critical.csv', 'r') as f:
    reader = csv.reader(f)
    csv_list = list(reader)
    headers = csv_list[0]

creation_date = headers.index('Created At')
severity = headers.index('Severity')
status = headers.index('Status')

counters = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for current in csv_list:
    if current[status] == "OPEN":
        if current[severity] == 'LOW':
            counters[0]+=1
        if current[severity] == 'MEDIUM':
            counters[1]+=1
        if current[severity] == 'HIGH':
            counters[2]+=1
        if current[severity] == 'CRITICAL':
            counters[3]+=1
    if current[status] == "IN_PROGRESS":
        if current[severity] == 'LOW':
            counters[4]+=1
        if current[severity] == 'MEDIUM':
            counters[5]+=1
        if current[severity] == 'HIGH':
            counters[6]+=1
        if current[severity] == 'CRITICAL':
            counters[7]+=1
    if current[status] == "RESOLVED":
        if current[severity] == 'LOW':
            counters[8]+=1
        if current[severity] == 'MEDIUM':
            counters[9]+=1
        if current[severity] == 'HIGH':
            counters[10]+=1
        if current[severity] == 'CRITICAL':
            counters[11]+=1
    if current[status] == "REJECTED":
        if current[severity] == 'LOW':
            counters[12]+=1
        if current[severity] == 'MEDIUM':
            counters[13]+=1
        if current[severity] == 'HIGH':
            counters[14]+=1
        if current[severity] == 'CRITICAL':
            counters[15]+=1

"""
print(f"\n\033[1mStatus: OPEN\033[0m\nLow: {counters[0]}\nMedium: {counters[1]}\nHigh: {counters[2]}\nCritical: {counters[3]}\n")
print(f"\n\033[1mStatus: IN_PROGRESS\033[0m\nLow: {counters[4]}\nMedium: {counters[5]}\nHigh: {counters[6]}\nCritical: {counters[7]}\n")
print(f"\n\033[1mStatus: RESOLVED\033[0m\nLow: {counters[8]}\nMedium: {counters[9]}\nHigh: {counters[10]}\nCritical: {counters[11]}\n")
print(f"\n\033[1mStatus: REJECTED\033[0m\nLow: {counters[12]}\nMedium: {counters[13]}\nHigh: {counters[14]}\nCritical: {counters[15]}\n")

"""

print(f"\nStatus: OPEN\nCritical: {counters[3]}\nHigh: {counters[2]}\nMedium: {counters[1]}\nLow: {counters[0]}\n")
print(f"Status: IN_PROGRESS\nCritical: {counters[7]}\nHigh: {counters[6]}\nMedium: {counters[5]}\nLow: {counters[4]}\n")
print(f"Status: RESOLVED\nCritical: {counters[11]}\nHigh: {counters[10]}\nMedium: {counters[9]}\nLow: {counters[8]}\n")
print(f"Status: REJECTED\nCritical: {counters[15]}\nHigh: {counters[14]}\nMedium: {counters[13]}\nLow: {counters[12]}\n")

