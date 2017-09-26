#!/usr/bin/python3

import sys
import re

#Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not. 
#The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010

def main():
  if len(sys.argv) == 1 or not re.search(r'^([01]{4},)*[01]{4}$',sys.argv[1]):
    print ('Usage ./012.py binary numbers comma-separated')
    return 1
    
  numbers = sys.argv[1].split(',') 
  result = []
  
  for x in numbers:
  	if int(x,2)%5 == 0:
  		result.append(x)

  print(','.join(result))

if __name__ == '__main__':
  main()

