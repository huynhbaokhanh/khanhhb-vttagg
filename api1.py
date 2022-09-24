import requests
import json

def api1_call():
  url = "https://apigateway-econtract-staging.vnptit3.vn/auth-service/oauth/token"

  payload = json.dumps({
    "grant_type": "client_credentials",
    "client_id": "test.client@econtract.vnpt.vn",
    "client_secret": "U30nrmdko76057dz5aQvV9ug0mTsqAQy"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  return response
