import sys

multiple_list = [x for x in range(1000) if (x % 3 == 0 or x % 5 == 0)]
a = sum(multiple_list)
print "The sum of the multiples list is: " + str(a)
