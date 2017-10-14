import datetime

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
    self.factString = factString
    self.factHash = factHash
    self.confidence = confidence
    
