from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# When someone visit the web with


# create a dictionary to store months and its tasks

month_task = {
    'january': 'This is January page - do not eat meat for the entire month!',
    'february': 'This is February page - take 20 min walk every day!',
    'march': 'This is  page - learn Django for 1 hour every day!',
    'april': 'This is  page - learn Django for 1 hour every day! 4',
    'may': 'This is  page - learn Django for 1 hour every day! 5',
    'june': 'This is  page - learn Django for 1 hour every day! 6',
    'july': 'This is  page - learn Django for 1 hour every day! 7',
    'august': 'This is  page - learn Django for 1 hour every day! 8',
    'september': 'This is  page - learn Django for 1 hour every day! 9',
    'october': 'This is  page - learn Django for 1 hour every day! 10',
    'november': 'This is  page - learn Django for 1 hour every day! 11',
    'december': 'This is  page - learn Django for 1 hour every day! 12',
}

# Create your views here.


def monthly_challenges(request, month):     # 'month' is a key word identifier for urls.py
    try:
        text = month_task[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Page not found.")
