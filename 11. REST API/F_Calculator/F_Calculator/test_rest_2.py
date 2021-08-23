import requests
import json


#Step1 : Request URL
url = 'https://reqres.in'
#Step2 : Headers.
headers = {'Content-Type': 'application/json'}


# API CALL 7  List Users:
# Perform REST API Call
print("---------API CALL 1  List Users----------")
resp = requests.get(url+'/api/users?page=2', headers=headers)

# Validate response headers and body contents, e.g. status code.
assert resp.status_code == 200
resp_body = resp.json()
print("Data from reqres website : ",resp_body)
#assert resp_body['url'] == url




# API CALL 7:
print("---------API CALL 7  CREATE----------")
#Step3 : Payload(Body)
payload = {"name": "Madhu","job": "Software Engineer"}

# Perform REST API Call
resp = requests.post(url+'/api/users', headers=headers, data=json.dumps(payload))

# Validate response headers and body contents, e.g. status code.
assert resp.status_code == 201
resp_body = resp.json()
print("Data from reqres website : ",resp_body)
#assert resp_body['url'] == url
