import math
from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import DoughCalculatorForm


def calculator(request):
    form = DoughCalculatorForm()
    dough = None
    if request.method == "POST":
        form = DoughCalculatorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            dough = {ing.replace('_', ' '): {'Percent': data[ing]} for ing in data if not ing.endswith('_set')}

            if data['dough_wt_set'] and data['choice_set'] == 'dough_wt':
                dough_wt = data['dough_wt_set']
            else:
                radius2 = (data['pizza_size_set'] / 2) ** 2
                dough_wt = data['thk_factor_set'] * Decimal(math.pi * radius2)

            total_pct = sum(val['Percent'] for val in dough.values())
            flour_wt = dough_wt * data['pizza_num_set'] / (total_pct / 100)

            dough |= {'total': {'Percent': total_pct}}
            for kv in dough.values():
                weight = flour_wt * (kv['Percent']) / 100
                kv['Grams'] = kv['Ounces'] = weight
                if data['g_oz_set'] == 'g' and data['choice'] == 'Dough Weight':
                    kv |= {'Ounces': weight * Decimal(0.03527396195)}
                else:
                    kv |= {'Grams': weight * Decimal(28.349523125)}

            print(dough)
            # return redirect('pizza-dough')
    context = {
        'form': form,
        'dough': dough
    }
    return render(request, 'pizzadough/calculator.html', context)


def calculate(request):
    return HttpResponse('placeholder')
