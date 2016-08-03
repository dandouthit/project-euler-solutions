import math

pal_sum = 0

def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

for i in xrange(1,1000000):
    dec_str = str(i)
    bin_str = bin(i)[2:]

    if check_palindrome(dec_str) and check_palindrome(bin_str):
        pal_sum += i

print pal_sum
