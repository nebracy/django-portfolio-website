from django.http import HttpResponse
from django.shortcuts import render
from .forms import DoughCalculatorForm


def calculator(request):
    form = DoughCalculatorForm()
    context = {
        'form': form
    }
    return render(request, 'pizzadough/calculator.html', context)
