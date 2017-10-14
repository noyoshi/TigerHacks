# Library for extracting article text into facts
from article import article
from fact import Fact
from source import Source

# Function for generating facts from article.
# @OUTPUT - list of facts
def extractFacts(article):
  facts = list()
  sentences = article.body.split(".")
  print sentences
  print len(sentences)
  return facts
