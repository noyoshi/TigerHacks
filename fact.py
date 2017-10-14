import datetime
from article import article
from source import Source

# Fact data structure
class Fact(object):
  def __init__(self, 
                published_date=datetime.date(year=1970,month=1,day=1),
                sources=list(),
                distilledFact="",
                factStrings=list(),
                factHash=0,
                confidence=0):
    self.published_date = published_date
    self.sources = sources
    self.distilledFact = distilledFact
    self.factStrings = factStrings
    self.factHash = factHash
    self.confidence = confidence


# Function for generating facts from article.
# @OUTPUT - list of facts
def extractFacts(article):
  facts = list()

  return facts
