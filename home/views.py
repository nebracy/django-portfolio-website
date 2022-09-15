from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .models import Commit


def index(request):
    db_commits = Commit.objects.order_by('-date').all()[:3]
    form = ContactForm()
    context = {
        'title': 'Home',
        'commits': db_commits,
        'form': form
    }
    return render(request, 'home/index.html', context)
