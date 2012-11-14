#!/usr/bin/env python

from string import find

def subStringMatchExact(target, key):
    foundAt = find(target, key)
    answer = ()
    if foundAt > -1:
        nextIndex = foundAt + 1
        subtarget = target[nextIndex:]
        subanswer = subStringMatchExact(subtarget, key)
        answer = (foundAt,) + tuple(map(lambda x: x + nextIndex, subanswer))
    return answer

print subStringMatchExact("atgacatgcacaagtatgcat","atgc")
assert subStringMatchExact("atgacatgcacaagtatgcat","atgc") == (5, 15)

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def printResult(x):
    print subStringMatchExact(x[0], x[1])

map(lambda x: printResult(x), [
    (target1, key10),
    (target1, key11),
    (target1, key12),
    (target1, key13),
    (target2, key10),
    (target2, key11),
    (target2, key12),
    (target2, key13)
])
