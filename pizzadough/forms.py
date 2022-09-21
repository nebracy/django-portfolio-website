from django import forms
from django.core.exceptions import ValidationError


TH_FACTOR_DOUGH_WT = [('dough_wt', 'Dough Weight'), ('th_factor', 'Thickness Factor')]
OUNCES_GRAMS = [('ounces', 'oz'), ('grams', 'g')]


class DoughCalculatorForm(forms.Form):
    choice_set = forms.ChoiceField(label='TF/Weight', label_suffix='', choices=TH_FACTOR_DOUGH_WT, initial='th_factor', widget=forms.RadioSelect)
    flour = forms.IntegerField(min_value=100, max_value=100, initial=100, widget=forms.HiddenInput)
    dough_wt_set = forms.DecimalField(label='Dough Weight', label_suffix='', min_value=1, max_value=20000, required=False)
    g_oz_set = forms.ChoiceField(choices=OUNCES_GRAMS, initial='grams', widget=forms.RadioSelect)
    thk_factor_set = forms.DecimalField(label='Thickness Factor', label_suffix='', widget=forms.NumberInput(attrs={'type': 'range', 'min': '0.07', 'max': '0.1', 'value': '0.09', 'step': '0.005'}))
    pizza_size_set = forms.IntegerField(label='Pizza Size (in)', label_suffix='', min_value=12, max_value=22, initial=16, required=False)
    pizza_num_set = forms.IntegerField(label='Pizza(s)', label_suffix='', min_value=1, max_value=25, initial=1)
    water = forms.IntegerField(label='Hydration', label_suffix='', widget=forms.NumberInput(attrs={'type': 'range', 'min': '55', 'max': '70', 'value': '61'}))
    yeast = forms.DecimalField(label='Yeast', label_suffix=' %', min_value=0, max_value=3, step_size=0.05, initial=0.5)
    salt = forms.DecimalField(label='Salt', label_suffix=' %', min_value=0, max_value=4, step_size=0.05, initial=1.5)
    olive_oil = forms.DecimalField(label='Olive Oil', label_suffix=' %', min_value=0, max_value=8, step_size=0.05, initial=3, required=False)
    sugar = forms.DecimalField(label='Sugar', label_suffix=' %', min_value=0, max_value=4, step_size=0.05, initial=1.5, required=False)

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get("choice_set") == 'dough_wt' and not cleaned_data.get("dough_wt_set"):
            raise ValidationError('Dough Weight is required.')
        elif cleaned_data.get("choice_set") == 'th_factor' and not cleaned_data.get("pizza_size_set"):
            raise ValidationError('Pizza Size is required.')
