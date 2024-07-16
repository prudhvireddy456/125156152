from django.shortcuts import render
from django.http import HttpResponse,request
from django.http import JsonResponse
import random
import json
# Create your views here.
global pre
global cur
def random1(request):
    x=[]
    pre=[]
    cur=[]
    for i in range(10):
        x.append(random.randrange(1,100,2))
    # import json
    # import requests
    # headers = {'Authorization':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzIxMTM5ODIzLCJpYXQiOjE3MjExMzk1MjMsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjhhNTM1NGY4LTlmN2ItNGI2YS1hY2ZmLWFiMjRkZDkyODM4OSIsInN1YiI6IjEyNTE1NjE1MkBzYXN0cmEuYWMuaW4ifSwiY29tcGFueU5hbWUiOiJTQVNUUkEiLCJjbGllbnRJRCI6IjhhNTM1NGY4LTlmN2ItNGI2YS1hY2ZmLWFiMjRkZDkyODM4OSIsImNsaWVudFNlY3JldCI6IlNCWWNZRFV5ckhaalJCZkUiLCJvd25lck5hbWUiOiJOYW5kdXJpIFBydWRodmkgUmVkZHkiLCJvd25lckVtYWlsIjoiMTI1MTU2MTUyQHNhc3RyYS5hYy5pbiIsInJvbGxObyI6IjEyNTE1NjE1MiJ9.PDMC6jYHYcqbqc8nGxgQvE-uvdqZ_eEGtah5JsjZmjk' }
    # res=requests.get('http://20.244.56.144/test/rand',headers=headers)
    # print(res.json())
    cur=x
    avg=sum(x)/len(x)
    d={
        'numbers':x,
        'windowPreState':pre,
        'windowCurrState':cur,
        'avg':avg
    }
    d=json.dumps(d)
    return JsonResponse(data=d,safe=False)

    
