#!/usr/bin/env python2.7

__author__= "Noah Yoshida"

import feedparser 
from datetime import datetime
import urllib
from bs4 import BeautifulSoup as soup 
from article import article

def nyt_scraper(my_url):
    '''
    Returns a list of article objects from the scraped BBC news URL
    You can chose different URLs for BBC RSS to serve up 
    '''
    # my_url =  # URL of rss feed / whatever you need

    uClient = urllib.urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,'xml')

    article_list = [] 

    for item in page_soup.findAll('item'): # For each RSS article  
        title = item.title.text.encode("utf-8")
        description = item.description.text.encode("utf-8")
        date = str(item.pubDate.text)
        link = item.link.text
        
        uClient = urllib.urlopen(link)
        page_html = uClient.read()
        uClient.close()
        page_soup = soup(page_html, "html.parser")
        stories = page_soup.findAll("p")
        body = ""

        for bod in stories: # Gets the strings from the paragraphs 
            body = body + bod.text
        if len(body) > 0:
            temp = article(title,description,date,link,body)
            article_list.append(temp)

    
    return article_list

# Testing purposes only
