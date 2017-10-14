#!/usr/bin/python

#############################
## FACT COMPARATOR LIBRARY ##
#############################

#ARE_COMPARABLE
# returns True if facts are related and can be compared
# returns False otherwise
def are_comparable(factA, factB):
  return factA.factHash == factB.factHash

#COMPARE FACTS
# returns True if the distilledFact strings match
# returns False otherwise
def compare_facts(factA, factB):
  if are_comparable(factA, factB):
    return factA.distilledFact == factB.distilledFact
