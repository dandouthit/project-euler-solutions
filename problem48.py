import sys
power_sum = 0

for i in range(1,1001):
    power_sum = power_sum + i**i

int_str = str(power_sum)

slice = int_str[-10:]

print "The last ten characters of the sum of the series are: " + slice
