import math
import sys

def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def filter_out_evens(n):
    for char in str(n):
        if char in ['0','2','4','6','8']:
            return False
    return True       

def filter_out_fives(n):
    for char in str(n):
        if char == '5':
            return False
    return True

def get_rotations(n):
    string_n = str(n)
    rotations = set()
    for i in range(len(string_n)):
        rotations.add(int(string_n[i:] + string_n[0:i]))
    return rotations

# define counter variable
j = 3
primes = []
odd_digit_primes = []
circular_primes = []


while j < 1000000:
    if isPrime(j):
        primes.append(j)
    # no need to check even numbers as they will never be prime after 2
    j = j+2


# can throw out all of the numbers that have even digits, as the rotation with the even digit as the last digit will not be prime
odd_digit_primes = [prime for prime in primes if filter_out_evens(prime)]

# throw out all of the numbers that have '5' as a digit, for the same logic 
filtered_primes = set([prime for prime in odd_digit_primes if filter_out_fives(prime)])

for prime in filtered_primes:
    rot_set = get_rotations(prime)
    if rot_set.issubset(filtered_primes):
        circular_primes.append(prime)

print circular_primes
### do this at the very end ###
# need to put 2 back into list after filtering out 'even digit numbers'
# need to put 5 back into list after filtering out '5' digit numbers
circular_primes.append(2)
circular_primes.append(5)

print "There are " + str(len(circular_primes)) + " circular primes below 1 million"
