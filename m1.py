import json
import requests
data={
    "companyName":"SASTRA",
    "ownerName":"Nanduri Prudhvi Reddy",
    "rollNo":"125156152",
    "ownerEmail":"125156152@sastra.ac.in",
    "accessCode":"LGcHvG"
}
data=json.dumps(data)
res=requests.post('http://20.244.56.144/test/register',data=data)
print(res.json())

