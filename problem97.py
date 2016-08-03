import sys

n = 2
for i in range(7830456):
    n = (2*n) % 10000000000

n *= 28433
n += 1

n = n % 10000000000


print "The last 10 digits of the big prime are: " + str(n)
