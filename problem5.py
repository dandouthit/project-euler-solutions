import math
import sys

# only need to check numbers smaller than 20! as by definition the factorial will suffice
# start the loop at 20 as any number small can't be divisible by 20 and only check even numbers
check_list = [11,13,14,16,17,18,19,20]

def find_solution(step):
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(20)
    print "The smallest number to be divided without remainder is: " + str(solution)
    
