from django.shortcuts import render
from django.http import HttpResponse
from .models import Commit


def index(request):
    db_commits = Commit.objects.order_by('-date').all()[:3]
    context = {
        'title': 'Home',
        'commits': db_commits
    }
    return render(request, 'home/index.html', context)
