# Filter new facts based on previously existing facts in the database
from article import article
from fact import Fact
from source import Source
import fact_comp_lib
import json

#LOAD DATABASE
def load_db(file_name):
  with open(file_name, 'r') as f:
    read_str = f.read()
    facts_db = json.loads(read_str)
  return facts_db

#DECODE THE UNICODE STRING
def decode_string(string):
  return_str = ""

  for s in string.strip():
    try:
      return_str += s.decode('utf-8')
    except:
      continue

  return return_str

#FILTER FACTS
def filter_facts(fact, fact_db):
  report = {}
  questioned = decode_string(fact.factStrings[0])
  max_similarity = 0.125

  for f in fact_db:
    accepted = decode_string(fact_db[f]['fact_strings'][0])
    confidence = fact_db[f]['confidence']
    similarity = fact_comp_lib.hash_check(questioned, accepted)

    if similarity > max_similarity:
      report = {"similarity": int(similarity*100), "questioned": questioned, "accepted": accepted, "confidence": int(confidence*100)}
      max_similarity = similarity

  return report
