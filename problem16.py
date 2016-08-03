big_number = 2 ** 1000

string = str(big_number)
sum = 0
for char in string:
    sum = sum + int(char)

print "The sum of the digits of the big number is: " + str(sum)
