from django.urls import path
from . import views

urlpatterns = [
    path(r"api/create", views.create, name="create"),
    path(r"<str:uuid>", views.get, name="get"),
]
