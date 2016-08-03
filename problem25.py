# 1000 digit Fibonacci number

import sys

# set the first two terms of the sequence
m = 1
n = 1

# counter j for the number of digits in the number in the sequence
j = 0

# set index counter
i = 2

while j < 1000:
    k = m + n
    j = len(str(k))
    # set m and n to be the new values
    m = n
    n = k
    i += 1

# print k
print i

