import sys

def fib(n):
  a,b = 1,1
  for i in range(n-1):
    a,b = b,a+b
  return a

def main():
  fib_list = []
  x = 1
  while fib(x) < 4000000:
    fib_list.append(fib(x))
    x += 1

  # remove the first item in the list to match the definition used by projecteuler.net
  fib_list.pop(0)
  a = sum([y for y in fib_list if y % 2 == 0])
  print "The sum of the even valued Fibonacci terms less than 4 million is: " + str(a)

if __name__ == '__main__':
  main()

