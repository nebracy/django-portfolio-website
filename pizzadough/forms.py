from django import forms


TH_FACTOR_DOUGH_WT = [('dough_wt', 'Dough Weight'), ('th_factor', 'Thickness Factor')]
OUNCES_GRAMS = [('ounces', 'oz'), ('grams', 'g')]


class DoughCalculatorForm(forms.Form):
    choice = forms.ChoiceField(label='TF/Weight', choices=TH_FACTOR_DOUGH_WT, initial='th_factor', widget=forms.RadioSelect)
    flour = forms.IntegerField(min_value=100, max_value=100, initial=100, widget=forms.HiddenInput)
    dough_wt = forms.DecimalField(label='Dough Weight', min_value=1, max_value=20000)
    g_oz = forms.ChoiceField(choices=OUNCES_GRAMS, initial='grams', widget=forms.RadioSelect)
    thk_factor = forms.DecimalField(label='Thickness Factor', widget=forms.NumberInput(attrs={'type': 'range', 'min': '0.07', 'max': '0.1', 'value': '0.09', 'step': '0.005)'}))
    pizza_size = forms.IntegerField(label='Pizza Size (in)', min_value=12, max_value=22, initial=16)
    pizza_num = forms.IntegerField(label='Pizza(s)', min_value=1, max_value=25, initial=1)
    water = forms.IntegerField(label='Hydration', widget=forms.NumberInput(attrs={'type': 'range', 'min': '55', 'max': '70', 'value': '61'}))
    yeast = forms.DecimalField(label='Yeast %', min_value=0, max_value=3, step_size=0.05, initial=0.5)
    salt = forms.DecimalField(label='Salt %', min_value=0, max_value=4, step_size=0.05, initial=1.5)
    olive_oil = forms.DecimalField(label='Olive Oil %', min_value=0, max_value=8, step_size=0.05, initial=3, required=False)
    sugar = forms.DecimalField(label='Sugar %', min_value=0, max_value=4, step_size=0.05, initial=1.5, required=False)
    # opt = forms.DecimalField(label='Ingredient', min_value=0, max_value=50, step_size=0.05, initial=0, required=False)
