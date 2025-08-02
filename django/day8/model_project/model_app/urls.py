from django.urls import path, URLPattern
from . import views

urlpatterns=[
    path("",view=views.home),
    path("getuser/",view=views.get_data),
    path("postuser/",view=views.post_user),
]