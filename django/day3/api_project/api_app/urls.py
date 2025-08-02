from django.urls import path

from . import views

urlpatterns=[
    path("get",view=views.get_view),
    path("post",view=views.post_view),
    path("put",view=views.put_view),
    path("delete",view=views.delete_view),
    path("patch",view=views.patch_view),

]