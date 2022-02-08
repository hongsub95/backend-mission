from rest_framework import serializers
from clothes import models
from markets import serializers as markets_serializers
from options import serializers as options_serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = ("name",)


class ClothesSerializer(serializers.ModelSerializer):

    market = markets_serializers.MarketSerialzer()
    category = CategorySerializer()
    size = options_serializers.SizeSerialzer(many=True)
    colors = options_serializers.ColorSerialzer(many=True)

    class Meta:
        model = models.Clothes
        exclude = ()
        read_only_fields = ("host", "pk", "created", "updated")

    def create(self, validated_data):
        request = self.context.get("request")
        clothes = models.Clothes.objects.create(**validated_data, host=request.host)
        return clothes

    def put(self, validated_data):
        pass
