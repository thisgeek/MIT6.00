#!/usr/bin/env python

def fill(length, val):
    return [val for i in range(length)]

# Candidate for tree search abstraction
def packs(n, co = [6, 9, 20]):
    coeffs = list(co)
    coeffs.sort() # coeffs must be in orders for efficient retrieval

    # When n is smaller than the smallest coeff, no solution exists
    if n < coeffs[0]:
        return []

    answer = fill(len(coeffs), 0)

    # See if n is a mulitple of one coeffs
    for coeff in coeffs:
        if n % coeff == 0:
            i = coeffs.index(coeff)
            answer[i] = n / coeff
            print coeff,"goes into",n,answer[i],"times"
            return answer

    # Try combinations of coeffs, starting with the largest
    while coeffs:
        largest = coeffs.pop()

        # Form the quotient
        quotient = n / largest
        print largest,"goes into",n,quotient,"times"

        if quotient < 1:
            continue

        # If n is divisible by largest, you're done
        if n % largest == 0:
            answer[len(coeffs)] = quotient
            return answer

        # If n isn't, try all zero or more multiples of largest up to
        # the quotient
        while quotient > -1:
            remaining = n - quotient * largest
            quotient = quotient - 1

            # Try combinations of the remaining coeffs with the current
            # quotient
            print 'remaining:',remaining,'coeffs:',coeffs
            if (coeffs):
                print "RECURSE"
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


def printPacks(n):
    print n,"\n",packs(n),"\n"
    #combo = packs(n)
    #if (len(combo):
    #    print combo[0],"6 packs |",combo[1],"9 packs |",combo[2],"20 packs"

map(lambda x: printPacks(x), [
    15, 16, 40, 49, 50, 51, 52, 53, 54, 55
])
