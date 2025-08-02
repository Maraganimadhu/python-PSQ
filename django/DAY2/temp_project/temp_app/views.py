from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

# fuction based views
def test(self):
    return HttpResponse("hello welcome ")   #httpresponse is take string format
    # return JsonResponse({"name":"madhu maragani","age":18})
def user_info(self):
    return JsonResponse({"name":"madhu maragani","age":18})
def gest(self):
    return HttpResponse("this is gest login in django")