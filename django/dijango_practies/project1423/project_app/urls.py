from django.urls import path,URLPattern
from .import views

Urlpattern=[
    path("test",view=views.test),
]