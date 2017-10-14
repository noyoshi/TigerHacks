#!/usr/bin/python

#############################
## FACT COMPARATOR LIBRARY ##
#############################

#ARE_COMPARABLE
# returns True if facts are related and can be compared
# returns False otherwise
def are_comparable(factA, factB):
  return factA.factHash == factB.factHash

#COMPARE DISTILLED
# returns True if the distilledFact strings match
# returns False otherwise
def compare_distilled(factA, factB):
  if are_comparable(factA, factB):
    return factA.distilledFact == factB.distilledFact
  else:
    return False

#COMPARE CONFIDENCE
# returns the fact with the higher confidence
def compare_confidence(factA, factB):
  if factA.confidence > factB.confidence:
    return factA
  else:
    return factB

#COMPARE FACTS
# return fact that has the higher confidence
def compare_facts(factA, factB):
  if compare_distilled(factA, factB):
    return compare_confidence(factA, factB)
  else:
    return False

#HASH CHECK
#
def hash_check():
  pass
