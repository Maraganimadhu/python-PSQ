from django.urls import path
from . import views

urlpatterns=[
    path('test',view=views.test),
    path('user_info',view=views.user_info),
    path("gest",view=views.gest),
]