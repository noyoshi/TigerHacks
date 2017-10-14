# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

import datetime

def index(request):
    return render(request, 'project/home.html')

def article(request):
    print "Running tests"
    title = request.GET.get('title')
    if title == None:
        title = ""

    description = request.GET.get('description')
    if description == None:
        description = ""

    dateStr = request.GET.get('date')
    if  dateStr == None:
        date = datetime.date(1970,1,1)
    else:
        date = datetime.date(1970,1,1)

    body = request.GET.get('body')
    if body == None:
        body = ""

    link = request.GET.get('link')
    if link == None:
       link = ""


    print(title)
    print(description)
    print(date)
    print(body)
    print(link)

    return render(request, 'project/article.html')

def reddit(request):
    link = request.GET.get('link')
    if link == None:
      link = ""
    
    print(link)

    return render(request, 'project/reddit.html')

