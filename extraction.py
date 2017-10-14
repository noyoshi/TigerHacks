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

parser = English() #instantiate one parser to reduce init times

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
 
  # Convert char by char to ignore individual non-ascii chars.
  newFactString = ""
  for c in factString.strip():
    try:
      newFactString = newFactString + c.decode('utf-8')
    except:
      continue
  for token in parser(newFactString):
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

# Creates a hash representation of a string distilling Nouns/sentiments.
def hashFact(factString):
  hashSet = set()
  newFactString = ""
  for c in factString.strip():
    try:
      newFactString = newFactString + c.decode('utf-8')
    except:
      continue
  for token in parser(newFactString):
    # print token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights]
    if token.dep_ == u'nsubj'  or token.dep_ == u'nobj' or token.dep_ == u'pobj':
      hashSet.add(token.orth_)
  if len(hashSet > 0):
    return hash(" ".join(hashSet))

  return hash(newFactString)


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
  facts = list()
  sentences = article.body.split('.')
  for s in sentences:
    c = checkability(s)
    if c > CHECK_THRESHOLD:
      facts.append(Fact(published_date=article.date,
                        distilledFact=str(distillFact(s)),
                        factStrings=[s],
                        factHash = hashFact(s),
                        confidence = c))
  return facts
