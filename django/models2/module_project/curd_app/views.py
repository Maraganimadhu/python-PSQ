from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from . models import EMPLOYEES
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return HttpResponse("it's working")
@csrf_exempt
# create
def getuser(request):
    data=json.loads(request.body)
    user_data=EMPLOYEES.objects.create(
    id=data["id"],
    name=data["name"],
    phone=data["phone"]
    )
    return JsonResponse({"id":"user_data_geted"})
@csrf_exempt
# update
def updateuser(request,id):
    data=json.loads(request.body)
    user_data=EMPLOYEES.objects.get(id=id)
    name=data["name"]
    phone=data["phone"]
    return HttpResponse("the data was updated successfully")

@csrf_exempt
# delete
def deleteuser(request,id):
    user_data=EMPLOYEES.objects.get(id=id)
    user_data.delete()
    return HttpResponse("the data was deleted successfully")

def read(request):
    user_data=EMPLOYEES.objects.all()
    return JsonResponse({"userdata":json.dumps(user_data)})

    

