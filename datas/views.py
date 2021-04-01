from django.shortcuts import render

from .models import Data


def index(request):
    return render(request, "index.html")
