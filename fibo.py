#!/usr/bin/python


def fib(n): # write Fibonacci series
  a, b = 0, 1
  while b < n:
    print b
    a, b = b , b + a



if __name__ == '__main__':
    fib(1000)
