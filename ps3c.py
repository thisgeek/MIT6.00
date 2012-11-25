#!/usr/bin/env python

from string import find
from types import StringType, IntType

def subStringMatchExact(target, key):
    assert type(target) is StringType
    assert type(key) is StringType
    answer = ()
    keyLength = len(key)
    # When key is longer than target, the answer is empty
    if (keyLength > len(target)):
        return answer
    # When key is an empty string, don't bother with find or recursion
    if (keyLength == 0):
        answer = tuple([i for i,x in enumerate(target)])
        print "found {} in {} at {}".format('EmptyString',target,answer)
        return answer

    foundAt = find(target, key)
    if foundAt > -1 and len(target) > 0:
        print "found {} in {} at {}".format(key,target,foundAt)
        nextIndex = foundAt + 1
        subtarget = target[nextIndex:]

        # Recurse, but avoid a stack limit exception
        assert len(subtarget) <= len(target), "{} is not a reduced form of {} and will exceed the recursion limit".format(subtarget, target1)
        subanswer = subStringMatchExact(subtarget, key)

        answer = (foundAt,) + tuple([x + nextIndex for x in subanswer])
    return answer

def constrainedMatchPair(firstMatch,secondMatch,length):
    assert type(length) is IntType
    firstMatch = tuple(sorted(firstMatch))
    secondMatch = tuple(sorted(secondMatch))
    answer = ()
    for n in firstMatch:
        sum = n + length + 1
        if sum in secondMatch:
            answer = answer + (n,)
    return answer

### the following procedure you will use in Problem 3

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers

# TESTS

## Test constrainedMatchPair

print "Should be (0,): {}".format(constrainedMatchPair((0,),(1,),0))
print "Should be (): {}".format(constrainedMatchPair((0,),(2,),0))

## Test subStringMatchOneSub

# target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

targets = (target1,target2)
keys = (key10,key11,key12,key13)

for target in targets:
    for key in keys:
        print "[ANSWER] target: {} | key: {} | result: {}\n".format(target,key,subStringMatchOneSub(key,target))

