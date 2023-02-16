from urllib import request
from django.shortcuts import render
from datetime import date


# Create your views here.
def index(request):
    ip = request.headers
    today = date.today()
    return render(request, 'index.html', {'ip2': ip, 'date': today})


def page(request, page):
    return render(request, 'index.html', {'page': page})


def calc(request, a, func, b):
    f = eval(func)
    sum = f(a, b)
    return render(request, 'index.html', locals())


def req(request):
    # items = {}
    ip = request.path_info
    # print(type(request.META))
    return render(request, 'index.html', {'ip': ip, 'dict': request.META})


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def python(request):
    return render(request, 'Python基础学习.html')
