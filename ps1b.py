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
        last = primes[len(primes) - 1]
        candidate = last + 2 # Need only try odds
        while not(isPrime(candidate, "byKnownPrimes")):
            candidate = candidate + 2
        assert isPrime(candidate)
        primes.append(candidate)
    return primes[n - 1]

# Log
from math import *

def sigmaLnPrimes(n):
    i = primes.index(n) - 1
    return reduce(lambda x, y: log(x) + y, primes[:i])

def printRatio(n):
    sum = sigmaLnPrimes(n)
    print "sum:",sum,"| n:",n,"| ratio:",sum/n

# Execute

nthPrime(5000)
map(lambda x: printRatio(x), [
    primes[10],
    primes[100],
    primes[200],
    primes[300],
    primes[400],
    primes[500],
    primes[600],
    primes[700],
    primes[800],
    primes[900],
    primes[999],
    primes[2000],
    primes[3000],
    primes[4000],
    primes[4999]
])
