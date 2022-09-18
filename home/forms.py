from django.conf import settings
from django.core.mail import EmailMessage
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subj = forms.CharField(label='Subject', max_length=100)
    msg = forms.CharField(label='Message', widget=forms.Textarea)

    def send_email(self):
        email_msg = EmailMessage(
            f"Contact Form: {self.cleaned_data.get('subj')}",
            self.cleaned_data.get('msg'),
            self.cleaned_data.get('email'),
            [settings.CONTACT_EMAIL],
            reply_to=[f"{self.cleaned_data.get('name')} <{self.cleaned_data.get('email')}>"]
        )
        email_msg.send()
