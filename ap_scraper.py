#!/usr/bin/env python2.7

__author__= "Noah Yoshida"

import feedparser 
from datetime import datetime
import urllib
from bs4 import BeautifulSoup as soup 
def ap_scraper():
    my_url = "http://feeds.bbci.co.uk/news/rss.xml" # URL of rss feed / whatever you need


    uClient = urllib.urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,'xml')

    titles = []
    descriptions = []
    dates = []

    for item in page_soup.findAll('item'):
        titles.append(item.title.text.encode("utf-8"))
        descriptions.append(item.description.text.encode("utf-8"))
        dates.append(str(item.pubDate.text))
    return [titles, descriptions, dates]

l = ap_scraper()
for i in range(len(l[0])):
    print l[0][i]
    print l[1][i]
    print l[2][i]
    print 