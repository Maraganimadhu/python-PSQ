import requests,json


rootURL="http://127.0.0.1:8000/user_info/"

data=requests.get(url=rootURL)
print(data.json())

