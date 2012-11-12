#!/usr/bin/env python

import logging

def log(*args):
    #print (' '.join(map(str, args)))
    #logging.info(' '.join(map(str, args)))
    pass

def fill(length, val):
    return [val for i in range(length)]

# Candidate for tree search abstraction
def packs(n, co = (6, 9, 20)):
    coeffs = list(co)
    coeffs.sort() # coeffs must be in order for efficient retrieval
    log("n:", n)

    # When n is smaller than the smallest coeff, no solution exists
    if n < coeffs[0]:
        return []

    answer = fill(len(coeffs), 0)

    # See if n is a mulitple of one coeff
    for coeff in coeffs:
        if n % coeff == 0:
            i = coeffs.index(coeff)
            answer[i] = n / coeff
            log(coeff, "goes into", n, answer[i], "times")
            return answer

    # Try combinations of coeffs, starting with the largest
    while coeffs:
        largest = coeffs.pop()

        # Form the quotient
        quotient = n / largest
        log(largest, "goes into", n, quotient, "times")

        if quotient < 1:
            continue

        # Try all zero or more multiples of largest up to the quotient
        while quotient > -1:
            remaining = n - quotient * largest
            quotient = quotient - 1

            # Try combinations of the remaining coeffs with the current
            # quotient
            log("remaining:", remaining, "coeffs:", coeffs)
            if (coeffs):
                log("RECURSE")
                subanswer = packs(remaining, coeffs)
                if (subanswer):
                    answer = list(subanswer)
                    answer.append(quotient + 1)
                    return answer
                else:
                    continue
            else:
                return [];

    return answer

def largestImpossibleTotal(tup):
    largest = 1
    i = 1
    consec = 0
    while consec < tup[0] or i > 1000:
        answer = packs(i, tup)
        if not(answer):
            print i-consec," +",consec,"failed"
            largest = i
            consec = 0
        else:
            print i-consec," +",consec,"succeeded"
            consec = consec + 1
        i = i + 1
    assert i <= 1000 # If we got to 1000 iterations, throw an exception
    print "Stopped looking after",i-1
    return largest

# Execute
def printPacks(n):
    print packs(n),"\n"

logging.getLogger().setLevel(logging.INFO)

#map(lambda x: printPacks(x), range(50,65))

tup = (6, 9, 20)
n = largestImpossibleTotal(tup)
print "For these coeffs:",tup
print "Largest number of McNuggets that cannot be bought in exact quantity:",n
