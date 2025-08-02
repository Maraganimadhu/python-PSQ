from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import users

user_data=users.user_list
# Create your views here.

def welcome(req):
    return HttpResponse("Welcome to curd app")

@csrf_exempt
def get_data(req):
    if req.method=="GET":
        if len(user_data)>0:
            return JsonResponse({"data":user_data})
        else:
            return JsonResponse({"msg":"data not found"})
    else:
        return JsonResponse({"msg":"invalid method "})
@csrf_exempt
def post_user(req):
    if req.method=="POST":
        reg_data=json.loads(req.body)
        # print(reg_data)
        try:
         if reg_data["username"] and reg_data["password"] and reg_data["email"] and reg_data["phone"]:
            details={
                "id":len(user_data)+1,
                "username":reg_data["username"],
                "password":reg_data["password"],
                "email":reg_data["email"],
                "phone":reg_data["phone"]
            }
            user_data.append(details)
            return HttpResponse("user registation successful")
        except Exception as e:
            print(e)

        else:
            return HttpResponse("missing values requied")
    else:
        return JsonResponse({"msg":"invalid method "})
@csrf_exempt
def patch_user(req,id):
    if req.method=="PATCH":
        data=json.loads(req.body)
        user_exist=False
        for i in user_data:
            if i["id"]==id:
                user_exist=True
                i["password"]=data["password"]
                return HttpResponse("password updated")
        if user_exist:
            return JsonResponse({"msg":"user not found"})



