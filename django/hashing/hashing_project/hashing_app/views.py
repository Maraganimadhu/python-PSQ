from django.contrib.auth import user_logged_in
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from .models import STUDENT
from django.views.decorators.csrf import csrf_exempt
from . serializer import STUDENTSerializer


# Create your views here.
def home(req):
    return HttpResponse("it's working madhu")
@csrf_exempt
def register(req):
    try:
        if req.method=="POST":
            user_data=json.loads(req.body)
            model_data=STUDENT.objects.create(
                id=user_data['id'],
                name=user_data['name'],
                email=user_data['email'],
                password=user_data['password'],
                phone=user_data['phone']
                )
    except Exception as e:
        return HttpResponse(str(e))
    return JsonResponse({"msg":"user registered successfully"})

def showuser(req):
    try:
        user_data=json.loads(req.body)
        stud_serializer=STUDENTSerializer(data=user_data)
        if stud_serializer.is_valid():
            stud_serializer.save()
    except Exception as e:
        return HttpResponse(str(e))
    return JsonResponse({"msg":"data was stored successfully"})

