# Distinct powers

import sys

powers = []

for a in range(2,101):
    for b in range(2, 101):
        powers.append(a**b)

uniq_list = list(set(powers))

print len(uniq_list)
