from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def index1(request):
    return render(request, 'temp1.html')
