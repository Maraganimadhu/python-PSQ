from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def get_view(req):
    return HttpResponse(f"your in {req.method} method ")
@csrf_exempt
def post_view(req):
    return HttpResponse(f"your in {req.method} method ")
@csrf_exempt
def patch_view(req):
    return HttpResponse(f"your in {req.method} method ")
@csrf_exempt
def delete_view(req):
    return HttpResponse(f"your in {req.method} method ")
@csrf_exempt
def put_view(req):
    return HttpResponse(f"your in {req.method} method ")