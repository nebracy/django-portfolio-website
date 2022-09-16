from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .forms import ContactForm
from .models import Commit


def index(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subj = f'Contact Form: {form.cleaned_data["subj"]}'
            msg = form.cleaned_data['msg']
            email_msg = EmailMessage(subj, msg, email, ["contact@nicolebracy.com"], reply_to=[f'{name} <{email}>'])
            email_msg.send()
            messages.success(request, 'Email sent, thank you!')
            return redirect('index')

    db_commits = Commit.objects.order_by('-date').all()[:3]
    context = {
        'title': 'Home',
        'commits': db_commits,
        'form': form
    }
    return render(request, 'home/index.html', context)


@require_POST
def webhook(request):

    return JsonResponse({})
