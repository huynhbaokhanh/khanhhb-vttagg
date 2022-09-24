import requests

def api9_call():
  url = "https://apigateway-econtract-staging.vnptit3.vn/esolution-service/contracts/create-draft-from-file-raw"

  payload={'customer': """{
      "email": "khanhhb.agg@gmail.com",
      "sdt": "094455399",
      "userType": "CONSUMER",
      "ten": "test email ne",
      "noiCap": "da nang",
      "tenToChuc": "to chuc test ne",
      "mst": "09924523299",
      "loaiGtId": "1",
      "noiCap": "",
      "soDkdn": "",
      "ngayCapSoDkdn": "2021-12-22",
      "noiCapDkkd": ""
    }""",
  'contract': """{
    "autoRenew": "true",
    "callbackUrl": "test url",
    "contractValue": "20000",
    "creationNote": "",
    "endDate": "2021-11-17",
    "flowTemplateId": "d4b7e398-586b-4364-8af0-2a1c869cd0f4",
    "sequence": 1,
    "signFlow": [
      {
        "signType": "DRAFT",
        "signForm": [
          "OTP",
          "EKYC",
          "OTP_EMAIL",
          "NO_AUTHEN",
          "EKYC_EMAIL",
          "USB_TOKEN",
          "SMART_CA"
        ],
        "userId": "thonv02@yopmail.com",
        "sequence": 1,
        "limitDate": 3
      },
      {
        "signType": "APPROVE",
        "signForm": [
          "OTP",
          "EKYC",
          "OTP_EMAIL",
          "NO_AUTHEN",
          "EKYC_EMAIL",
          "USB_TOKEN",
          "SMART_CA"
        ],
        "departmentId": "",
        "userId":"nhansu02@yopmail.com",
        "sequence": 2,
        "limitDate": 3
      }
    ],
    "signForm": [
      "USB_TOKEN",
        "SMART_CA"
    ],
    "templateId": "632d2482eacefaff53042098",
    "title": "Hợp đồng AGG - KHANHHB",
    "validDate": "2021-11-17",
    "verificationType": "NONE",
    "fixedPosition": false
  }""",
  'fields': '{}'}
  files=[
    ('',('filepdf.pdf',open('filepdf.pdf','rb'),'application/pdf'))
  ]
  headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsidGVtcGxhdGUiLCJpYW0iLCJkc2lnbiIsInJlc3RzZXJ2aWNlIl0sInNjb3BlIjpbInJlYWQiLCJ3cml0ZSJdLCJyb2xlcyI6WyJURVNUIl0sImV4cCI6MTY2NDA3NjUzMSwicGFydHlJZCI6IjI2NzFkYzkxLTUxNzUtNGM4ZC1hOTAxLTBmZTAxYWMxZTQxZCIsImF1dGhvcml0aWVzIjpbIlRFU1QiXSwianRpIjoiYmFlNmJmNjItNTYxNi00YTE5LTg0OGYtNzFlOTM2MjgwMjI0IiwiY2xpZW50X2lkIjoidGVzdC5jbGllbnRAZWNvbnRyYWN0LnZucHQudm4ifQ.IWZxU-PLUNgBnNp9gonpDRSyZyCRS8Lc0S4ccgs5L8TyGNt67kVbY8vz4xJC0KbbHphNpx5SUFcHEtqquKhfDq3g7Ol6rLvAvvIX2tZoP71eJUOIycCmVXdW4zZ1AQG1UD-6oz4nTlmBFe4qqGF_bZG5fM3NZkK0YzPWaDwG23cPLMINfmN6cii-CJxzKVR26cdaCfRSFRW3UuHP4A0kdKjQxMc07ACtivWaKjKJd_c3rnIYlFpdmPGLIntMHKV5YI9dUlzTfDxnV-CxqOXKnvnJxhQ76VPpOpBhmzdeml7u5Q6vw8jqigoQ4oHDkWfZUyC_VAx6poDQ-g6NOQrzHQ'
  }

  response = requests.request("POST", url, headers=headers, data=payload, files=files)
  return response