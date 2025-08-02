from django.urls import path
from . import views


urlpatterns=[
    path("",view=views.home),
    path("postdata/",view=views.postdata),
    path("getdata/",view=views.getdata),
]
