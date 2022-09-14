from django.shortcuts import render
from django.http import HttpResponse
from .models import Commit


def index(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home/index.html', context)
