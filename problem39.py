import sys
import math
from collections import Counter

# from basic math, c can be no larger than 997

def isSquare(n):
    return math.sqrt(n) % 1 == 0

triplet = []
lengths = []

for b in range(1,1001):
    for a in range(1,b-1):
        sq_sum = a**2 + b**2
        if isSquare(sq_sum):
            root = math.sqrt(sq_sum)
            if a+b+root <= 1000:
                triplet.append((a, b, root))
                lengths.append(a+b+root)

print "Most common length is: " + str(Counter(lengths).most_common(1))

