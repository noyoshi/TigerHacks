#!/usr/bin/python

import make_db, filter_f, extraction, nyt_scraper, bbc_scraper, json

db_url = "http://feeds.bbci.co.uk/news/politics/rss.xml"
ck_url = "http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"

#MAKE DATABASE (should only happen once)
print "Making database... URL: {}".format(db_url)
facts_db = make_db.make_db(db_url)

#LOAD DATABASE
print "Loading Database..."
facts_db = filter_f.load_db('facts_db.json')

#SCRAPE URL
print "Scraping... URL: {}".format(ck_url)
articles = nyt_scraper.nyt_scraper(ck_url)
#articles = bbc_scraper.bbc_scraper(ck_url)

#EXTRACT FACTS
for article in articles:
  facts = extraction.extractFacts(article)
  #PASS THROUGH FILTER
  for fact in facts:
    report = filter_f.filter_facts(fact, facts_db)
    #DELIVER REPORT
    if report != {}:
      print "Fact Being Questioned: {}".format(report['questioned'])
      print "Accepted Fact: {}".format(report['accepted'])
      print "Similarity: {}% | Confidence Score: {}%".format(report['similarity'], report['confidence'])
      print "Source: {} | {}".format(report['source']['title'], report['source']['link'])
      print
