from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('Hello World')

def goodbye(request):
    return HttpResponse('Goodbye')

def index(request):
    return HttpResponse('Это главная страница')