from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from . import serializers
from clothes import models


class ListClothesView(ListAPIView):
    queryset = models.Clothes.objects.all()
    serializer_class = serializers.ClothesSerializer
