#!/usr/bin/python


def fib2(n):
  result = []
  a, b = 0, 1
  while b < n:
    result.append(b)
    a, b = b, b + a
  return result

if __name__ == '__main__':
    fib2(1)
