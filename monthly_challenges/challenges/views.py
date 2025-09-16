from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
        html_text = f'<h1>{text}</h1>'
        return HttpResponse(html_text)
    except:
        return HttpResponseNotFound("<h1>Page not found.</h1>")


def monthly_challenges_num(request, month):
    months = list(month_task.keys())        # dictionary are ordered since certain version
    if month > len(months) or month < 1:
        return HttpResponseNotFound('<h1>PAGE NOT FOUND</h1>')
    redirect_to_month = months[month-1]
    construct_path = reverse('month-url', args=[redirect_to_month])     # month-url - challenges, args = january / feb etc
    return HttpResponseRedirect(construct_path)
