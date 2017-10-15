#!/usr/bin/python

import make_db

#BBC URLS
top = "http://feeds.bbci.co.uk/news/rss.xml"
politics_b = "http://feeds.bbci.co.uk/news/politics/rss.xml"

#NYT URLS
home = "http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
us = "http://rss.nytimes.com/services/xml/rss/nyt/US.xml"
politics = "http://rss.nytimes.com/services/xml/rss/nyt/Politics.xml"

facts_dict = {}

#get dicts of facts

#BBC
top_facts = make_db.add_bbc(top)
politics_b_facts = make_db.add_bbs(politics_b)

#NYT
home_facts = make_db.add_nyt(home)
us_facts = make_db.add_nyt(us)
politics_facts = make_db.add_nyt(politics)

#join dicts into one large json database
facts_dict.update(top_facts)
facts_dict.update(politics_b_facts)
facts_dict.update(home_facts)
facts_dict.update(us_facts)
facts_dict.update(politics_facts)

#write to file
with open('facts_db.json', 'w') as f:
  f.write(json.dumps(facts_dict))
