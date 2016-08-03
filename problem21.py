def d(n):
    the_sum = 0
    for i in range(1,n):
        if n%i == 0: the_sum += i
    return the_sum
                     
total = 0
for i in range(1, 10000):
    x = d(i) 
    y = d(x)
    if i == y and i != x:
        total += i

print "The sum of the amicable numbers below 10000 is: " + str(total)

