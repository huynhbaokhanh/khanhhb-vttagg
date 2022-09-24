import requests
import json

def api2_call():
  url = "https://apigateway-econtract-staging.vnptit3.vn/auth-service/oauth/token"

  payload = json.dumps({
    "grant_type": "password",
    "client_id": "test.client@econtract.vnpt.vn",
    "username": "khanhhb.agg@gmail.com",
    "client_secret": "U30nrmdko76057dz5aQvV9ug0mTsqAQy",
    "password": "U5BeY9Xq",
    "domain": "econtract-staging.vnptit3.vn"
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  return response
