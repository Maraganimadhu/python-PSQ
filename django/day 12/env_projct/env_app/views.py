from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import EMPLOY
from django.views.decorators.csrf import csrf_exempt
from .serializers import EmpSerializer
# Create your views here.

def home(req):
    return HttpResponse("its working")
@csrf_exempt
def postdata(req):
    user_daa=json.loads(req.body)
    print(user_daa)
    model_data=EMPLOY.objects.create(
        id=user_daa['id'],
        emp_name=user_daa['emp_name'],
        emp_mob=user_daa['emp_mob']
    )
    return HttpResponse("data was posted is successfully",status=201)

def getdata(req):
    try:
        model_data=EMPLOY.objects.all()
        serilizer=EmpSerializer(data=model_data)
        print(serilizer.is_valid())
        if serilizer.is_valid():
            serilizer.save()
            return JsonResponse(serilizer.data)
        # print(json.dumps(model_data))
    except Exception as e:
        return HttpResponse("get data error")
    return HttpResponse(f"{serilizer.data}")

# def get_employe(req,id):
#     try:
#         modell=EMPLOY.objects.get(id=id)
#         new_data=EmpSerializer(modell)
#         return JsonResponse({'data':new_data.data})
#     except Exception as e:
#         return HttpResponse("error",f"{e}")
