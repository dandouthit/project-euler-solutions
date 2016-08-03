import sys

max_digital_sum = 1

def digit_sum(power):
    string = str(power)
    sum = 0
    for char in string:
        sum = sum + int(char)

    return sum

for a in range(1,100):
    for b in range(1,100):
        power = a**b
        sum = digit_sum(power)
        if sum > max_digital_sum:
            max_digital_sum = sum

print "The maximum digital sum is: " + str(max_digital_sum)
