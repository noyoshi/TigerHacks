#!/usr/bin/python

#############################
## FACT COMPARATOR LIBRARY ##
#############################

#ARE_COMPARABLE
# returns True if facts are related and can be compared
# returns False otherwise
def are_comparable(factA, factB):
  if factA.factHash == factB.factHash:
    return True
  else:
    return False
