from django.urls import path
from. import views
urlpatterns=[
    path("",view=views.welcome),
    path("getuser/",view=views.get_data),
    path("postuser/",view=views.post_user),
    path("patchuser/<int:id>",view=views.patch_user),
]