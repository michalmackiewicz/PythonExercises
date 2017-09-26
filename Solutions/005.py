#!/usr/bin/python3

import sys
import re

#Write a program which accepts a sequence of comma-separated numbers
#and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

def main():
  if len(sys.argv) == 1 or not re.search(r'^(\d+,)*\d+$',sys.argv[1]):
    print ('Usage ./005.py numbers comma separated')
    return 1
    
  results = sys.argv[1].split(',') 

  print(results)

  results_tuple = tuple(results)

  print(results_tuple)

if __name__ == '__main__':
  main()

