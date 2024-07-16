import json
import requests
data={'companyName': 'SASTRA', 'clientID': '8a5354f8-9f7b-4b6a-acff-ab24dd928389', 'clientSecret': 'SBYcYDUyrHZjRBfE', 'ownerName': 'Nanduri Prudhvi Reddy', 'ownerEmail': '125156152@sastra.ac.in', 'rollNo': '125156152'}
data=json.dumps(data)
res=requests.post('http://20.244.56.144/test/auth',data=data)
print(res.json())