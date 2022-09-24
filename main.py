from os import access
from urllib import response
import api1, api9, api10, api2, api11

respone_api1 = api1.api1_call()

print("access token khoi tao: " + respone_api1.json()['access_token'])

respone_api9 = api9.api9_call()
contractId = respone_api9.json()['object']['contractId']
title = respone_api9.json()['object']['title']
print("contractId: " + contractId)
print("ten hop dong: " + title)

respone_api10 = api10.api10_call(contractId)
if respone_api10.status_code == 204:
    print("Gui hop dong thanh cong")

respone_api2 = api2.api2_call()
access_token_2 = respone_api2.json()['access_token']
print("access token 2: " + access_token_2)

respone_api11 = api11.api11_call(contractId, access_token_2)
if respone_api11.status == 204:
    print("Upload va cap nhat trang thai file thanh cong")