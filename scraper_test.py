#!/usr/bin/env python2.7

__author__= "Noah Yoshida"

import feedparser 
from datetime import datetime
import urllib
from bs4 import BeautifulSoup as soup 
from article import article


uClient = urllib.urlopen("http://feeds.bbci.co.uk/news/rss.xml")
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,'xml')

titles = []
descriptions = []
dates = []
links = []
for item in page_soup.findAll('item'): # I can make this better space efficiency and time 
    print item.link.text
    links.append(item.link.text)
for link in links: # Go to all of the links!
    uClient = urllib.urlopen(link)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "xml")
    stories = page_soup.findAll("div",{"class":"story-body__inner"})
    body = ""
    for bod in stories:
        paragraphs = bod.findAll("p")
        for pars in paragraphs:
            body = body + pars.text
    print body 

#     titles.append(item.title.text.encode("utf-8"))
#     descriptions.append(item.description.text.encode("utf-8"))
#     dates.append(str(item.pubDate.text))
# l = [titles, descriptions, dates]

# article_list = []
# for i in range(len(l[0])):
#     temp = article(l[0][i],l[1][i],l[2][i])
#     article_list.append(temp)

# for thing in article_list:
#     print thing 