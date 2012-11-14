#!/usr/bin/env python

from string import find

def countSubStringMatch(target, key):
    count = 0
    lowestIndex = find(target, key)
    while lowestIndex > -1:
        count = count + 1
        lowestIndex = find(target, key, lowestIndex + 1)
    print "{} instances of {} in {}".format(count, key, target)
    return count

def countSubStringMatchRecursive(target, key):
    foundAt = find(target, key)
    if foundAt > -1:
        print "found {} in {} at {}".format(key, target, foundAt)
        return countSubStringMatchRecursive(target[foundAt + 1:], key) + 1
    else:
        return 0

# Test

assert countSubStringMatch('aaa', 'b') == 0
assert countSubStringMatch('aaa', 'aa') == 2
assert countSubStringMatch('abba', 'ba') == 1
assert countSubStringMatch('abbaabba', 'ba') == 2
assert countSubStringMatch('abababab', 'aba') == 3

assert countSubStringMatchRecursive('aaa', 'b') == 0
assert countSubStringMatchRecursive('aaa', 'aa') == 2
assert countSubStringMatchRecursive('abba', 'ba') == 1
assert countSubStringMatchRecursive('abbaabba', 'ba') == 2
assert countSubStringMatchRecursive('abababab', 'aba') == 3
