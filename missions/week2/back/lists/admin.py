from django.contrib import admin
from . import models


@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
    list_display = ("user", "Clothes_upper", "Clothes_pants", "Clothes_shoes")
    filter_horizontal = ("clothes_Upper", "clothes_Pants", "clothes_Shoes")
    raw_id_fields = ("user",)

    def Clothes_upper(self, obj):
        upper = obj.clothes_Upper.all()
        list_upper = []
        if upper:
            for li in upper:
                list_upper.append(li)
            return list_upper if len(list_upper) < 5 else list_upper[:4]
        else:
            return list_upper

    Clothes_upper.short_description = "상의"

    def Clothes_pants(self, obj):
        pants = obj.clothes_Pants.all()
        list_pants = []
        if pants:
            for li in pants:
                list_pants.append(li)
            return list_pants if len(list_pants) < 5 else list_pants[:4]
        else:
            return list_pants

    Clothes_pants.short_description = "하의"

    def Clothes_shoes(self, obj):
        shoes = obj.clothes_Shoes.all()
        list_shoes = []
        if shoes:
            for li in shoes:
                list_shoes.append(li)
            return list_shoes if len(list_shoes) < 5 else list_shoes[:4]
        else:
            return list_shoes

    Clothes_shoes.short_description = "신발"
