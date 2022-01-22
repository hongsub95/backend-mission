from re import template
from django.db.models import Q
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import DetailView
import random
from . import models


def all_clothes(request):
    clothes_set = set()
    clothes = models.Clothes.objects.all()
    len_clothes = len(clothes)
    if len_clothes <= 10:
        clothes_set.update(clothes)
        return render(
            request,
            "clothes/home.html",
            context={
                "clothes_set": clothes_set,
                "clothes": clothes,
            },
        )
    else:
        for _ in range(10):
            num = random.randint(0, len_clothes - 1)
            clothes_set.add(clothes[num])
    return render(
        request,
        "clothes/home.html",
        context={
            "clothes_set": clothes_set,
            "clothes": clothes,
        },
    )


def clothes_list(request):
    page = request.GET.get("page", 1)
    clothes_list = models.Clothes.objects.all()
    paginator = Paginator(clothes_list, 10)
    try:
        clothes = paginator.get_page(page)
        return render(
            request,
            "clothes/clothes_list.html",
            context={"clothes": clothes},
        )
    except EmptyPage:
        return redirect("/")  # home으로 이동


class clothes_detail(DetailView):
    model = models.Clothes


def search(request):
    clothes_list = models.Clothes.objects.all()
    search = request.GET.get("search", "")
    if search:
        search_list = clothes_list.filter(
            Q(name__icontains=search) | Q(market__icontains=search)
        )
    paginator = Paginator(search_list, 10)
    return render(request, "clothes/search.html", {"search": search})
