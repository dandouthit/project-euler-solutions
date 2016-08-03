import sys
import math

# from basic math, c can be no larger than 997

def isSquare(n):
    return math.sqrt(n) % 1 == 0

triplet = []

for b in range(2,998):
    for a in range(1,b-1):
        sq_sum = a**2 + b**2
        if isSquare(sq_sum):
            root = math.sqrt(sq_sum)
            if root > b and root < 998 and a+b+root == 1000:
                triplet.append((a, b, root))

print triplet
print triplet[0][0] * triplet[0][1] * triplet[0][2]
