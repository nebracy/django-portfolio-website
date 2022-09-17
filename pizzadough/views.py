from django.http import HttpResponse
from django.shortcuts import render


def calculator(request):
    return HttpResponse('Test')
