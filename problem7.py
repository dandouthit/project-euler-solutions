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

while i < 10001:
    if isPrime(j):
        i = i+1
    j = j+1

j = j-1

print "The 10001st prime number is: " + str(j)
