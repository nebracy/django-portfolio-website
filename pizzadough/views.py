import math
from decimal import Decimal
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_POST
from .forms import DoughCalculatorForm


@require_GET
def calculator(request):
    context = {
        'form': DoughCalculatorForm()
    }
    return render(request, 'pizzadough/calculator.html', context)


@require_POST
def calculate(request):
    form = DoughCalculatorForm(request.POST)

    if not form.is_valid():
        return HttpResponse(status=204)

    data = form.cleaned_data
    recipe_table = {ing.replace('_', ' '): {'Percent': data[ing]} for ing in data if not ing.endswith('_set')}

    if data['dough_wt_set'] and data['choice_set'] == 'dough_wt':
        dough_wt = data['dough_wt_set']
    else:
        radius2 = (data['pizza_size_set'] / 2) ** 2
        dough_wt = data['thk_factor_set'] * Decimal(math.pi * radius2)

    total_pct = sum(val['Percent'] for val in recipe_table.values())
    flour_wt = dough_wt * data['pizza_num_set'] / (total_pct / 100)

    recipe_table |= {'total': {'Percent': total_pct}}
    for kv in recipe_table.values():
        weight = flour_wt * (kv['Percent']) / 100
        kv['Grams'] = kv['Ounces'] = weight
        if data['g_oz_set'] == 'g' and data['choice'] == 'Dough Weight':
            kv |= {'Ounces': weight * Decimal(0.03527396195)}
        else:
            kv |= {'Grams': weight * Decimal(28.349523125)}
    return render(request, 'pizzadough/table.html', {'recipe_table': recipe_table})
