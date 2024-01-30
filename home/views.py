from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    context = { 'fruits': Fruits.objects.all()}
    return render(request, 'home.html', context)
