# Library for extracting article text into facts
import requests
import json
import string
import spacy
from spacy.en import English

from article import article
from fact import Fact
from source import Source

FACT_CHECK_URL="http://idir-server2.uta.edu/claimbuster/API/score/text/"
CHECK_THRESHOLD=0.00

def buildClause(baseToken):
  output = baseToken.orth_
  if output in string.punctuation:
    return ""
  reverseLefts = list()
  for t in reversed(list(baseToken.lefts)):
    output = buildClause(t) + " " + output
  for t in baseToken.rights:
    output = output + " " + buildClause(t)

  return output

# Function to reduce a factual statment to a simple representation of the fact/quantities.
def distillFact(factString):
  sentenceRoot = None
 
  parser = English() 
  for token in parser(factString.strip().decode('utf-8')):
    #print token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights]
    if token.dep_ == "ROOT":
      sentenceRoot = token

  if sentenceRoot == None:
    return "" 

  bestString = ""  

  for t in sentenceRoot.lefts:
    testFact = buildClause(t)
    if len(testFact) > len(bestString):
      bestString = testFact
  for t in sentenceRoot.rights:
    testFact = buildClause(t)
    if len(testFact) > len(bestString):
      bestString = testFact

    return bestString

# Generates a score to determine how open to fact-checking a statement is.
def checkability(factString):
    r = requests.get(FACT_CHECK_URL+factString.strip().replace(" ", "+"), headers={'Content-Type':'application/json'})
    try:
      resp = json.loads(r.text)
      return resp['results'][0]['score']
    except:
      return -1


# Function for generating facts from article.
# @OUTPUT - list of facts
def extractFacts(article):
  parser = English()

  facts = list()
  sentences = article.body.split('.')
  for s in sentences:
    c = checkability(s)
    if c > CHECK_THRESHOLD:
      facts.append(Fact(published_date=article.date,
                        distilledFact=str(distillFact(s)),
                        factStrings=[s],
                        confidence = c))
  return facts
