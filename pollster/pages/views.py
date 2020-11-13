# Creates a main landing page
from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')
