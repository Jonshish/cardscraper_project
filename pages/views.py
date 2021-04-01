from django.shortcuts import render
from django.http import HttpResponse
from datas.models import Data


def index(request):
    datas = Data.objects.all()

    context = {"datas": datas}

    return render(request, "pages/index.html", context)


def login(request):
    return render(request, "pages/login.html")


def register(request):
    return render(request, "pages/register.html")


def password(request):
    return render(request, "pages/password.html")
