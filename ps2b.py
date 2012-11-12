#!/usr/bin/env python

def log(*args):
    pass

def fill(length, val):
    return [val for i in range(length)]

# Candidate for tree search abstraction
def packs(n, co):
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

# Execute

bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes

def largestImpossibleTotal():
    smallest = min(packages)

    for n in range(1, 200):   # only search for solutions up to size 150
        consec = 0
        if consec >= smallest:
            break

        answer = packs(n, packages)
        if not(answer):
            bestSoFar = n
            consec = 0
        else:
            consec = consec + 1
    return bestSoFar

def printPacks(tup):
    global packages
    global bestSoFar
    packages = tup
    bestSoFar = 0
    n = largestImpossibleTotal()
    packList = '{}, {}, and {},'.format(*packages)
    print "Given package sizes",packList,"the largest number of McNuggets that cannot be bought in exact quantity is:",n

map(lambda x: printPacks(x), [
    (6,9,20),
    (7,8,10),
    (2,6,31)
])

