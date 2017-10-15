#!/usr/bin/python

import spacy
from spacy.en import English
from fact import Fact

#############################
## FACT COMPARATOR LIBRARY ##
#############################

parser = English()

#ARE_COMPARABLE
# returns True if facts are related and can be compared
# returns False otherwise
#def are_comparable(factA, factB):
#  return factA.factHash == factB.factHash

#COMPARE DISTILLED
# returns True if the distilledFact strings match
# returns False otherwise
#def compare_distilled(factA, factB):
#  if are_comparable(factA, factB):
#    return factA.distilledFact == factB.distilledFact
#  else:
#    return False

#COMPARE CONFIDENCE
# returns the fact with the higher confidence
#def compare_confidence(factA, factB):
#  if factA.confidence > factB.confidence:
#    return factA
#  else:
#    return factB

#COMPARE FACTS
# return fact that has the higher confidence
#def compare_facts(factA, factB):
#  if compare_distilled(factA, factB):
#    return compare_confidence(factA, factB)
#  else:
#    return False

#HASH CHECK
def hash_check(factA, factB):
  A = []
  B = []
  a_str = ""
  b_str = ""
  
  #tokenize fact strings
  for a in factA.strip():
    try:
      a_str += a.decode('utf-8')
    except:
      continue
  for b in factB.strip():
    try:
      b_str += b.decode('utf-8')
    except:
      continue
  for token in parser(a_str):
    A.append(token)
  for token in parser(b_str):
    B.append(token)

  #check for common words
  count = 0.0
  for token in A:
    if token in B:
      if token.pos_ == 'PROPN':
        count += 1.0
      else:
        count += 0.5
  return_val = float((2 * float(count)) / (len(A) + len(B)))
  return return_val
