#!/usr/bin/python

# Package
primes = list()
primes.append(2)
primes.append(3)

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

# Test
assert isPrime(1)
assert isPrime(3)
assert not(isPrime(4))
assert isPrime(691)
assert not(isPrime(1001))

# Execute
n = 1000
nth = nthPrime(n)
print "The",n,"th prime is",nth
