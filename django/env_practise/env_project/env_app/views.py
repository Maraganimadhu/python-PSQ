from logging import exception

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from.models import EMPLOYEE
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(req):
    return HttpResponse("its working")


# entering data in table
@csrf_exempt
def postdata(req):
    try:
        user_data=json.loads(req.body)
        emp=EMPLOYEE.objects.create(
        id=user_data["id"],
        emp_name=user_data["emp_name"],
        emp_age=user_data["emp_age"]        
    )
    except exception as e:
        return JsonResponse({"error":str(e)})
    else:
        return HttpResponse("user data entered is sucuss")

def getdata(req,id):
    user=EMPLOYEE.objects.get(id=id)
    print(json.dumps(user))
    return JsonResponse({"data":user})
    