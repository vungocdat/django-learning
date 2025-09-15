from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# When someone visit the web with

# Create your views here.


def monthly_challenges(request, month):     # 'month' is a key word identifier for urls.py
    text = None
    if month == 'january':
        text = 'This is January page - do not eat meat for the entire month!'
    elif month == 'february':
        text = 'This is February page - take 20 min walk every day!'
    elif month == 'march':
        text = 'This is March page - learn Django for 1 hour every day!'
    else:
        return HttpResponseNotFound("This page does not exists!")
    return HttpResponse(text)
