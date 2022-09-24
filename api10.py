import requests
import json

def api10_call(contractId):
  url = "https://apigateway-econtract-staging.vnptit3.vn/esolution-service/contracts/" + contractId + "/submit-contract"

  payload = ""
  headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsidGVtcGxhdGUiLCJpYW0iLCJkc2lnbiIsInJlc3RzZXJ2aWNlIl0sInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJyb2xlcyI6WyJURVNUIl0sImV4cCI6MTY2NDAxMTA1NCwicGFydHlJZCI6IjI2NzFkYzkxLTUxNzUtNGM4ZC1hOTAxLTBmZTAxYWMxZTQxZCIsImF1dGhvcml0aWVzIjpbIlRFU1QiXSwianRpIjoiNjFmZWZhZGUtMWRmOS00ZjI0LThlYWEtZTU0NDFkYzJmNGIxIiwiY2xpZW50X2lkIjoidGVzdC5jbGllbnRAZWNvbnRyYWN0LnZucHQudm4ifQ.FMSWyZMMVbsFbxtxChGyKnU0Bo1wFlOu_Uz128h-1r2u_c-bC7VuyIWbrqFF-ZYFeWMeLZcuwfU0wmOmdC5sh87ABMw_itZekVOHhVNoSBBZMRqUxTbSGnI-m9Qq-96GJbqtUUc4XuazNZVVLt42BumFiekqXcaUJji4uzRvZ-oi2CLnHJ3uowix9Vf3eac6oa0WW0UOrHBFIQKXxS-To0r41Tsx0gUY-abKhJkASDEuZyR53TmUaTctTOyRuK9ueO7_E0vrD1qYtuLzHjzGxcM1kkbMxZsvTQeR4ZHyj5CahR2paaPqg5O-FjFyLAPPGXxVxIxifVmuoPkyHhRvSA'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  return response