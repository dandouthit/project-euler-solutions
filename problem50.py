# Project Euler problem #50

import sys

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(1000000)
sorted_primes = sorted(primes)

print sorted_primes
