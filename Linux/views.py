from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hi chandan how are you")

def index1(request):
    return HttpResponse("I am good ")