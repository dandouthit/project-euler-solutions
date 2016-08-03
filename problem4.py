max = 0

for x in xrange(100,1000):
    for y in xrange(100,1000):
        if str(x*y) == str(x*y)[::-1]:
            if x*y > max:
                max = x*y
                a = x
                b = y

print "The largest palindrome is: " + str(max)
print "The factors of the palindrome are: " + str(a) + " and " + str(b)
