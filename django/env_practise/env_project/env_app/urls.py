from .import views
from django.urls import path

urlpatterns=[  
    path("",view=views.home),
    path("send/",view=views.postdata),
    path("getdata/<int:id>",view=views.getdata),
]