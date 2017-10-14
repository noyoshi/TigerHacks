#!/usr/bin/python
#Create txt file with the article objects

from bbc_scraper import bbc_scraper
from extraction import extractFacts
import json

def make_db(url):

  articles = bbc_scraper(url)

  facts_dict = {}
  
  for article in articles:
    facts = extractFacts(article)
    for fact in facts:
      facts_dict[fact.factHash] = fact

  with open('facts_db.json', 'w') as f:
    f.write(json.dumps(facts_dict))
