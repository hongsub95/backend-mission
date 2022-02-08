from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from clothes import models


class ClothesViewset(viewsets.ModelViewSet):
    queryset = models.Clothes.objects.all()
    serializer_class = serializers.ClothesSerializer
