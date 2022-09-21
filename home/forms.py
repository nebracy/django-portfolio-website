from django.conf import settings
from django.core.mail import EmailMessage
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    subj = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    msg = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'Message'}))

    def send_email(self):
        email_msg = EmailMessage(
            f"Contact Form: {self.cleaned_data.get('subj')}",
            self.cleaned_data.get('msg'),
            self.cleaned_data.get('email'),
            [settings.CONTACT_EMAIL],
            reply_to=[f"{self.cleaned_data.get('name')} <{self.cleaned_data.get('email')}>"]
        )
        email_msg.send()
