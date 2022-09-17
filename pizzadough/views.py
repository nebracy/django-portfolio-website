from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import DoughCalculatorForm


def calculator(request):
    form = DoughCalculatorForm()
    if request.method == "POST":
        form = DoughCalculatorForm(request.POST)
        if form.is_valid():
            print('OK')
            return redirect('pizza-dough')
    context = {
        'form': form
    }
    return render(request, 'pizzadough/calculator.html', context)
