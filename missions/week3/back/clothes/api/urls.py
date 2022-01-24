from django.urls import path
from . import views

app_name = "clothes_api"

urlpatterns = [path("", views.ListClothesView.as_view(), name="clothes_api_list")]
