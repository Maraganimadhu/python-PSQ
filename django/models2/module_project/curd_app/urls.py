from django.urls import path
from . import views

urlpatterns=[
    path("",view=views.home),
    path("getusers/",view=views.getuser),
    path("updateuser/<int:id>",view=views.updateuser),
    path("deleteuser/<int:id>",view=views.deleteuser),
    path("read/",view=views.read),
]
