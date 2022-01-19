from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):
    clothes_Upper = models.ManyToManyField(
        "clothes.Upper",
        verbose_name="상의",
        related_name="list",
        blank=True,
    )
    clothes_Pants = models.ManyToManyField(
        "clothes.Pants",
        verbose_name="바지",
        related_name="list",
        blank=True,
    )
    clothes_Shoes = models.ManyToManyField(
        "clothes.Shoes",
        verbose_name="신발",
        related_name="list",
        blank=True,
    )
    user = models.ForeignKey("users.User", verbose_name="고객", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "장바구니"

    def __str__(self):
        return f"{self.user}님의 장바구니"
