from django.urls import path, URLPattern
from . import views

urlpatterns=[
    path("user_info",view=views.user),
]
