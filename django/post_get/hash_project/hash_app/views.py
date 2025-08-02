from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from.models import USER
from.serializer import Userserilizer
from django.views.decorators.csrf import csrf_exempt
import json
import bcrypt

# Create your views here.
def home(request):
    return HttpResponse('hello')
@csrf_exempt
def postdata(req):
    try:
        if req.method=="POST":
            user_data=json.loads(req.body)
            password=user_data['password'].encode("utf-8")
            salt=bcrypt.gensalt(12)
            hashed_password=bcrypt.hashpw(password,salt)
            user_data['password']=hashed_password.decode("utf-8")
            print(hashed_password)
            print(user_data)
            serilizer=Userserilizer(data=user_data)
            if serilizer.is_valid():
                print("entered if ")
                serilizer.save()
                print(serilizer.data)
                # return JsonResponse(serilizer.data)
            else:
                return HttpResponse("invalid data")

        else:
            return HttpResponse("method is invalid")
    except Exception as e:
        return HttpResponse(str(e))
    else:
        return HttpResponse("data stored successfully=")
def getdata(req):
    try:
        get_data=json.loads(req.body)


