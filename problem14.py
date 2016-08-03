# implemenation of Collatz sequences for starting points up to one million
import sys

def even_step(curr_step):
    return curr_step / 2

def odd_step(curr_step):
    return 3*curr_step + 1

# initialize chain length counter and generator variable
chain_len = 1
gen = 1

# start loop at 2 as a step of one has a trivial chain
for i in xrange(2,1000001):
    chain = [i]
    j = i
    while j != 1:
        # choose even_step function if current_step is even, else choose the odd_step function
        if j % 2 == 0:
            j = even_step(j)
        else:
            j = odd_step(j)

        chain.append(j)
        
    # if we have the longest chain so far, replace the chain_len variable and exit the while loop, storing the generator
    if len(chain) > chain_len:
        chain_len = len(chain)
        gen = i

print "The starting number that generates the longest chain is: " + str(gen)
