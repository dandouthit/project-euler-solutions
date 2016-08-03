import math
import sys

sum_of_squares = sum([x*x for x in range(1,101)])
print sum_of_squares

list = range(1,101)
list_sum = sum(list)
squared_of_sums = list_sum*list_sum
print squared_of_sums

print "The difference between the two is: " + str(squared_of_sums - sum_of_squares)
