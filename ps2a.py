#!/usr/bin/env python

import logging

def isInt(x):
    return x % 1 == 0

def log(*args):
    #print (' '.join(map(str, args)))
    logging.info(' '.join(map(str, args)))

def fill(length, val):
    return [val for i in range(length)]

# Candidate for tree search abstraction
def packs(n, co = [6, 9, 20]):
    coeffs = list(co)
    coeffs.sort() # coeffs must be in orders for efficient retrieval
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

        # If n isn't, try all zero or more multiples of largest up to
        # the quotient
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


# Execute
def printPacks(n):
    print n,"\n",packs(n),"\n"

logging.getLogger().setLevel(logging.INFO)

map(lambda x: printPacks(x), [
    15, 16, 40, 49, 50, 51, 52, 53, 54, 55
])
