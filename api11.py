# import requests

# def api11_call(contractId, access_token_2):
#   url = "https://apigateway-econtract-staging.vnptit3.vn/esolution-service/contracts/" + contractId + "/digital-sign"

#   payload={}
#   files=[
#     ('file',('filepdf.pdf',open('filepdf.pdf','rb'),'application/pdf'))
#   ]
#   headers = {
#     'Authorization': 'Bearer ' + access_token_2
#   }

#   response = requests.request("POST", url, headers=headers, data=payload, files=files)
#   return response

import http.client
import mimetypes
from codecs import encode

def api11_call(contractId, access_token_2):
  conn = http.client.HTTPSConnection("apigateway-econtract-staging.vnptit3.vn")
  dataList = []
  boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
  dataList.append(encode('--' + boundary))
  dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('filepdf.pdf')))

  fileType = mimetypes.guess_type('filepdf.pdf')[0] or 'application/octet-stream'
  dataList.append(encode('Content-Type: {}'.format(fileType)))
  dataList.append(encode(''))

  with open('filepdf.pdf', 'rb') as f:
    dataList.append(f.read())
  dataList.append(encode('--' + boundary))
  dataList.append(encode('Content-Disposition: form-data; name=data;'))

  dataList.append(encode('Content-Type: {}'.format('text/plain')))
  dataList.append(encode(''))

  dataList.append(encode("""{
  \"SignForm\":\"OTP_EMAIL\",
  \"name\": \"Huỳnh Bảo Khánh\",
  \"taxCode\":\"1231231234\",
  \"provider\": \"Công Ty VNPT\",
  \"pathImg\": \"iVBORw0KGgoAAAANSUhEUgAAAZAAAAJYCAYAAABM7LCIAABym\",
  \"identifierCode\": \"1231231234\", 
  \"phone\":\"0917881199\",
  \"email\":\"khanhhb.agg@gmail.com\",
  \"phone\":\"0917881199\",
  \"status\": \"VALID\",
  \"signType\": \"APPROVAL\",
  \"ekycInfo\": \"APPROVAL\"
  }"""))
  dataList.append(encode('--'+boundary+'--'))
  dataList.append(encode(''))
  body = b'\r\n'.join(dataList)
  payload = body
  headers = {
    'Authorization': 'Bearer ' + access_token_2,
    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
  }
  conn.request("POST", "/esolution-service/contracts/" + contractId + "/digital-sign", payload, headers)
  res = conn.getresponse()
  return res