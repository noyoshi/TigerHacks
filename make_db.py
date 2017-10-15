#!/usr/bin/python
#Create txt file with the article objects

from bbc_scraper import bbc_scraper
from nyt_scraper import nyt_scraper
from extraction import extractFacts
import json

def make_json(fact):
  fact_json = {}
  fact_json['published_date'] = str(fact.published_date)
  fact_json['distilled_fact'] = fact.distilledFact
  fact_json['fact_strings'] = fact.factStrings
  fact_json['confidence'] = fact.confidence
  fact_json['factHash'] = fact.factHash
  fact_json['sources'] = fact.sources

  return fact_json

def add_bbc(url):

  articles = bbc_scraper(url)
  facts_dict = {}
  
  for article in articles:
    facts = extractFacts(article)
    for fact in facts:
      fact_json = make_json(fact)
      facts_dict[fact.factHash] = fact_json

  return facts_dict

def add_nyt(url):

  articles = nyt_scraper(url)
  facts_dict = {}
  
  for article in articles:
    facts = extractFacts(article)
    for fact in facts:
      fact_json = make_json(fact)
      facts_dict[fact.factHash] = fact_json

  return facts_dict
