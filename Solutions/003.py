#!/usr/bin/python3

import sys
import re

#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

def fact(x):
  result = 1
  for y in range(0, x):
  	result = result * (y+1)
  return result

def main():

  if len(sys.argv) == 1 or not re.search(r'^(\d+,)*\d+$',sys.argv[1]):
  	print ('Calculates factorial of n \nUsage ./003.py numbers split by commas')
  	return 1

  results = []
  for x in sys.argv[1].split(','):
    n = int(x)
    result.append(str(fact(n)))

  print(', '.join(results))

if __name__ == '__main__':
  main()

