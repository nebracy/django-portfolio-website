from django.http import HttpResponse
from django.shortcuts import render


def calculator(request):
    return render(request, 'pizzadough/calculator.html')
