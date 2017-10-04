#!/usr/bin/python3

import sys
import re

# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 3.55
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Hints:
# Use float() to convert an integer to a float

def main():
  if len(sys.argv) == 1 or not re.search(r'^\d+$',sys.argv[1]):
    print ('Usage ./028.py number')
    return 1

  n = int(sys.argv[1])
  result = 0.0

  if n>0:
  	for x in range(n):
  		print(str(x+1))
  		result = result + (x+1)/(x+2)

    


  print(str(result))

if __name__ == '__main__':
  main()

