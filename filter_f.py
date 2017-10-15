# Filter new facts based on previously existing facts in the database
from article import article
from fact import Fact
from source import Source
import fact_comp_lib
import json

def load_db(file_name):
  with open(file_name, 'r') as f:
    read_str = f.read()
    facts_db = json.loads(read_str)
  return facts_db

def filter_facts(fact, fact_db):
  report = {}

  A = fact.factStrings[0]
  for f in fact_db:
    B = fact_db[f]['fact_strings'][0]
    similarity = fact_comp_lib.hash_check(A, B)
    if similarity > 0.3:
      report = {"similarity": similarity, "A": A, "B": B}

  return report
