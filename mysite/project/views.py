# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.conf import settings

from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

import json
import article as a
import filter_f
import extraction
import nyt_scraper
import bbc_scraper

import reddit_scraper

DB_URL = "http://feeds.bbci.co.uk/news/rss.xml"
CK_URL = "http://feeds.bbci"
facts_db = filter_f.load_db(os.path.join(settings.PROJECT_ROOT,'Data/facts_db.json'))

def index(request):
    return render(request, 'project/home.html')

def article(request):
    print "Running tests"
    description = request.GET.get('description')
    if description == None:
        return render_to_response('project/article.html', {'description': description})

    queryArticle = a.article(body=description)
    facts = extraction.extractFacts(queryArticle)
    reports = []
    for fact in facts:
      reports.append(filter_f.filter_facts(fact, facts_db))

    print "Reports: {}".format(reports)

    return render_to_response('project/article.html', {'description': description, 'reports':reports})

def reddit(request):
    link = request.GET.get('link')
    if link == None:
      return render_to_response('project/reddit.html', {'reports':None})
    
    print link

    posts = reddit_scraper.reddit_scraper(link) 

    print posts

    reports = []
    for p in posts:
      report = []
      facts = extraction.extractFacts(p)
      for f in facts:
        report.append(filter_f.filter_facts(fact, facts_db))
      
      reports.append({"first":p,"second":report,"length":len(report)})

    print reports

    return render_to_response('project/reddit.html', {'reports':reports,'length': len(reports)})

