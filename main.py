#!/usr/bin/python

import make_db

bbc_url = "http://feeds.bbci.co.uk/news/politics/rss.xml"
nyt_url = "http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"

facts_db = make_db.make_db(bbc_url, nyt_url)
