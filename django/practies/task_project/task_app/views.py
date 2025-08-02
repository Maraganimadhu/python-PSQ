from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.

def user(request):
    return JsonResponse({"name":"madhu","age":21,"batch":"37r"})