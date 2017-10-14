from extraction import hashFact

print hashFact("Christmas is a time of year")
print hashFact("This sentence is about Christmas")
print hashFact("Christmas is the worst time of year")

print hashFact("Christmas is a time of year") == hashFact("Christmas is the worst time of year")
print hashFact("Christmas is a time of year") == hashFact("Christmas isn't the worst time this year")
