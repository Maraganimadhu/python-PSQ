from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
# Create your views here.

user_data=[]
def home(request):
    return HttpResponse("it's working")
def get_data(req):
    if req.method== "GET":
       data=json.loads(req.body)
       print(data)
       return HttpResponse("data fetceh")
def post_user(req):
    if req.method== "POST":
        data = json.loads(req.body)
        user_data.append(data)
        print(user_data)
        return HttpResponse("data posted")



