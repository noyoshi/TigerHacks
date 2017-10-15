#!/usr/bin/python

import fact_comp_lib 

testA = "The brown fox dies near the tree"

testB1 = "The bike shop manager went to the store and bought some tires"
testB2 = "The man who manages the bike shop bought tires yesterday afternoon"

print "testA: {}".format(fact_comp_lib.hash_check(testA, testA))

print "testB: {}".format(fact_comp_lib.hash_check(testB1, testB2))
