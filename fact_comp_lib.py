#!/usr/bin/python

import spacy
from spacy.en import English
from fact import Fact

#############################
## FACT COMPARATOR LIBRARY ##
#############################

parser = English()

def calculate_similarity(nouns, verbs, other, X, total):
  total -= X
  weights = (float(nouns) * 1) + (float(verbs) * 0.75) + (float(other) * 0.5) * 2
  return weights / float(total)

#HASH CHECK
def hash_check(factA, factB):
  A = []
  B = []
  
  #tokenize fact strings
  for token in parser(factA):
    A.append(token)
  for token in parser(factB):
    B.append(token)

  #check for common words
  nouns = 0
  verbs = 0
  other = 0
  X     = 0
  b_tokens = 0
  a_tokens = 0
  
  #check how many of each kind of word are in both strings
  for token in A:

    a_tokens += 1
    if token.pos_ == 'DET' or token.pos_ == 'CONJ' or token.pos_ == 'CCONJ':
      X += 1
    elif token.pos_ == 'SCONJ' or token.pos_ == 'PUNCT' or token.pos_ == 'SYM':
      X += 1
    elif token.pos_ == 'ADP':
      X += 1

    elif token in B:
      if token.pos_ == 'PROPN' or token.pos_ == 'NOUN':
        nouns += 1
      elif token.pos_ == 'VERB':
        verbs += 1
      else:
        other += 1

  for token in B:

    b_tokens += 1
    if token.pos_ == 'DET' or token.pos_ == 'CONJ' or token.pos_ == 'CCONJ':
      X += 1
    elif token.pos_ == 'SCONJ' or token.pos_ == 'PUNCT' or token.pos_ == 'SYM':
      X += 1
    elif token.pos_ == 'ADP':
      X += 1
    

  total = a_tokens + b_tokens

  similarity = calculate_similarity(nouns, verbs, other, X, total)
  return similarity
