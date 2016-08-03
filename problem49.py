import math

def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# define counter variable
i = 0
j = 2
four_digit_primes = []
tuples = []

while i < 10001:
    if isPrime(j) and len(str(j)) == 4:
        four_digit_primes.append(j)
        i = i+1
    # stop once we hit the five digit prime numbers
    if len(str(j)) == 5:
        break
    j = j+1

# print four_digit_primes

m = len(four_digit_primes) - 1

for n in range(m,-1,-1):
    j = four_digit_primes[n]
    for a in range(n-1,-1,-1):
        i = four_digit_primes[a]
        k = j + (j-i)
        if k < 10000 and k in four_digit_primes:
            tuples.append((i,j,k))

# print tuples

for triple in tuples:
    a = str(triple[0])
    b = str(triple[1])
    c = str(triple[2])

    if sorted(a) == sorted(b) == sorted(c):
        target_triple = triple
        break

print target_triple
print a + b + c
