from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from clothes import models as clothes_models
from . import models
