#!/usr/bin/python3

import sys
import re

#Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
#Suppose the following input is supplied to the program:
#1,2,3,4,5,6,7,8,9
#Then, the output should be:
#1,3,5,7,9

def main():
  if len(sys.argv) == 1 or not re.search(r'^(\d+,)*\d+$',sys.argv[1]):
    print ('Usage ./016.py numbers comma-separated')
    return 1
    
  numbers = sys.argv[1].split(',') 

  result = [x for x in numbers if int(x)%2 != 0]

#   
#  for x in numbers:
#  	if int(x)%2 != 0:
#  		result.append(x)

  print(','.join(result))

if __name__ == '__main__':
  main()

