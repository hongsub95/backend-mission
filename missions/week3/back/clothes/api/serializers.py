from rest_framework import serializers
from clothes import models
from markets import serializers as markets_serializers


class ClothesSerializer(serializers.ModelSerializer):

    market = markets_serializers.MarketSerialzer()

    class Meta:
        model = models.Clothes
        fields = (
            "name",
            "price",
            "stock",
            "market",
            "host",
        )
