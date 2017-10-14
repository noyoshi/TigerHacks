# Library for extracting article text into facts
import spacy
from spacy.en import English

from article import article
from fact import Fact
from source import Source

# Function for generating facts from article.
# @OUTPUT - list of facts
def extractFacts(article):
  parser = English()

  facts = list()
  sentences = article.body.split(".")
  print len(sentences)
  
  for s in sentences:
    for token in parser(s.decode('utf-8')):
      if token.dep_ == 'quantmod':
        print s
        print token.orth_, token.dep_, token.head.orth_, [t.orth_ for t in token.lefts], [t.orth_ for t in token.rights]
        
        return facts

  return facts
