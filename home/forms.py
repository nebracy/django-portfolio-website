from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subj = forms.CharField(label='Subject', max_length=100)
    msg = forms.CharField(label='Message', widget=forms.Textarea)
