#!/usr/bin/python3

import re

# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def main():
    
  result = []
  
  for x in range(1000,3001):
    if re.search(r'^[02468]+$',str(x)):
      result.append(str(x))

  print(','.join(result))

if __name__ == '__main__':
  main()

