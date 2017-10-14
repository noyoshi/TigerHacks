#!/usr/bin/env python2.7

__author__= "Noah Yoshida"

import feedparser 
from datetime import datetime
import urllib
from bs4 import BeautifulSoup as soup 
from comment import comment
from comment import post 
import re 


def reddit_scraper(my_url):
    '''
    returns an array where the first element is the post (comment object) and the rest is
    comment objects about a news article 
    '''
    uClient = urllib.urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    stories = page_soup.findAll("div",{"class":"entry unvoted"})
    regex  = re.compile(".*?\((.*?)\)")
    body = ''
    author = ""
    children = []
    for thing in stories[::-1]:
        derp = thing.findAll("p")
        for x in derp:
            z = re.findall(regex,x.text)
            d = [[s.encode("utf-8", "ignore") for s in p] for p in z]
            result = x.text
            if len(d) > 0:
                print "AUTHOR: " + author
                print "BODY: " + body
                children.insert(0,comment(author,body))
                body = ""
                author = ""
                if ''.join(d[0])[0].strip().isdigit(): #is children a digit?

                    kids = int(''.join(d[0]).split()[0]) # NOT USING THIS ANYMORE, MAYBE IN THE FUTURE
                    # We are not implementing a heirarchy, instead we are just saying that all comments 
                    # are on the same level. 
                else: # else, we know that this is the end of the page(beginning I should say) 
                    author = ''.join(d[0])
                if len(re.sub("[\(\[].*?[\)\]]", "", result).encode("utf-8","ignore")) > 0:
                    author = ''.join(re.sub("[\(\[].*?[\)\]]", "", result).encode("utf-8","ignore")).split()[0]

            else:
                if len(re.sub("[\(\[].*?[\)\]]", "", result).encode("utf-8","ignore").split()) > 0 and "submitted" == re.sub("[\(\[].*?[\)\]]", "", result).encode("utf-8","ignore").split()[0]:
                    derp = re.sub("[\(\[].*?[\)\]]", "", result).encode("utf-8","ignore").split()
                    author =  derp[len(derp)-1]
                else:
                    body += re.sub("[\(\[].*?[\)\]]", "", result).encode("utf-8","ignore")

    return children

############## TESTING SHIT ######################
# news = reddit_scraper("https://www.reddit.com/r/leagueoflegends/comments/76c789/prediction_what_would_be_the_next_riot_steps_of/")
# news = reddit_scraper("https://www.reddit.com/r/news/comments/76c7e3/school_district_pulls_to_kill_a_mockingbird_from/")
# print news
# print news[0].get_author()
# print news[1].get_author()
