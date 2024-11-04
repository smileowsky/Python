from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'title': 'Home',
        'content': 'Main Page of Home',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_autenticated': False
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')
  