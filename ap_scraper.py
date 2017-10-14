#!/usr/bin/env python2.7

__author__= "Noah Yoshida"

import feedparser 
from datetime import datetime
import urllib
from bs4 import BeautifulSoup as soup 
from article import article
def ap_scraper(my_url):
    '''
    returns a list of article objects from the scraped AP news URL
    you can chose different URLs for Associated Press RSS to serve up 
    '''

    # my_url = "http://feeds.bbci.co.uk/news/rss.xml" # URL of rss feed / whatever you need

    uClient = urllib.urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,'xml')

    titles = []
    descriptions = []
    dates = []
    links = []
    for item in page_soup.findAll('item'): # I can make this better space efficiency and time 
        titles.append(item.title.text.encode("utf-8"))
        descriptions.append(item.description.text.encode("utf-8"))
        dates.append(str(item.pubDate.text))
        links.append(item.title.text)
    l = [titles, descriptions, dates, links]

    article_list = []
    for i in range(len(l[0])):
        temp = article(l[0][i],l[1][i],l[2][i],l[3][i])
        article_list.append(temp)
    
    return article_list
  

    # print l[0][i]
    # print l[1][i]
    # print l[2][i]
    # print 
# for thing in article_list:
#     print thing 
#     print 