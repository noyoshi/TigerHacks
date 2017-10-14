#!/usr/bin/python
#Create txt file with the article objects

from bbc_scraper import bbc_scraper
from extraction import extractFacts

def make_db(url):

  articles = bbc_scraper(url)
  
  with open('facts_db.txt', 'w') as f:
    for article in articles:
      facts = extractFacts(article)
      for fact in facts:
        f.write(fact)
