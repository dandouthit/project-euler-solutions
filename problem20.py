import math
big_number = math.factorial(100)

string = str(big_number)
sum = 0
for char in string:
    sum = sum + int(char)

print "The sum of the digits of the big number is: " + str(sum)
