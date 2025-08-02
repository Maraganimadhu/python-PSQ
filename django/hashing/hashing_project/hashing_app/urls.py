from django.urls import path
from.import views
urlpatterns=[
    path("",view=views.home),
    path("postdata/",view=views.register),
    path("getdata/",view=views.showuser)
]