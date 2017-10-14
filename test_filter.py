#!/usr/bin/python

import json
import filter_f, make_db
from fact import Fact

#write random fact to database
random = Fact()
r_hash = {}
r_hash[random.factHash] = make_db.make_json(random)
with open('facts_db_t.json', 'w') as t:
  t.write(json.dumps(r_hash))

print "loading database..."
facts_db = filter_f.load_db('facts_db_t.json')

print "filtering facts..."
filter_f.filter_facts(random, facts_db)
