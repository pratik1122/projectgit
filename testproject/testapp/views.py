from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse('hello')


def home(request):
    return HttpResponse('home')


def new(request):
    return HttpResponse('new')