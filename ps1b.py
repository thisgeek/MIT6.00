#!/usr/bin/python

# Package
primes = [2, 3]

def isInt(x):
    return x % 1 == 0

def isPrimeByHalf(x):
    assert isInt(x)
    i = x / 2
    while i > 1:
        if x % i == 0:
            return False
        i = i - 1
    return True

def isPrimeByKnownPrimes(x):
    assert isInt(x)
    for prime in primes:
        if x != prime and x % prime == 0:
            return False
    return True

def isPrime(x, by="byHalf"):
    if (by == "byKnownPrimes"):
        return isPrimeByKnownPrimes(x)
    else:
        return isPrimeByHalf(x)

def nthPrime(n):
    while len(primes) < n:
        last = primes[-1]
        candidate = last + 2 # Need only try odds
        while not(isPrime(candidate, "byKnownPrimes")):
            candidate += 2
        assert isPrime(candidate)
        primes.append(candidate)
    return primes[n - 1]

# Log
from math import log

def sigmaLnPrimes(n):
    i = primes.index(n) - 1
    return reduce(lambda x, y: log(x) + y, primes[:i])

def printRatio(n):
    sum = sigmaLnPrimes(n)
    print "sum: {} | n: {} | ratio: {}".format(sum, n, sum/n)

# Execute

nthPrime(5000)
map(lambda x: printRatio(primes[x]), [
    10,
    100,
    200,
    300,
    400,
    500,
    600,
    700,
    800,
    900,
    999,
    2000,
    3000,
    4000,
    4999
])
