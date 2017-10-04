#!/usr/bin/python3

import sys
import re

# Write a program which accepts a text as input to print the words composed of digits only.
# Example:
# If the following words is given as input to the program:
# 2catsand3dogs.
# Then, the output of the program should be:
# ['2', '3']
# Use re.findall() to find all substring using regex.

def main():
  if len(sys.argv) == 1:
    print ('Usage ./027.py text')
    return 1

  result = []    
  for x in re.findall(r'\d+',sys.argv[1]):
  	result.append(x)

  print(result)

if __name__ == '__main__':
  main()

