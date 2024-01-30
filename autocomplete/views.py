from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def index(request):
    return render(request, "index.html")


def get_names(request):
    search = request.GET.get('search')
    payload = []
    if search:
        objs = Names.objects.filter(name__startswith = search)

        for obj in objs:
            payload.append({
                'name' : obj.name 
            })

    return JsonResponse({
        'status': True,
        'payload': payload
    })

