from django.urls import path
from . import views

app_name = "lists"
urlpatterns = [
    path("add/<int:clothes_pk>", views.add_list, name="add_list"),
    path("", views.list_detail, name="list_detail"),
]
