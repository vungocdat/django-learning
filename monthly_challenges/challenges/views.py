from django.shortcuts import render
from django.http import HttpResponse

# When someone visit the web with

# Create your views here.


def jan(request):
    return HttpResponse('This is January page - do not eat meat for the entire month!')


def feb(request):
    return HttpResponse('This is February page - take 20 min walk every day!')
