#!/usr/bin/python3

import sys
import re

# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=1
# with a given n input by console (n>0).
# Example:
# If the following n is given as input to the program:
# 5
# Then, the output of the program should be:
# 501

def f(n):
  if n==0: return 1
  return f(n-1)+100

def main():
  if len(sys.argv) == 1 or not re.search(r'^\d+$',sys.argv[1]):
    print ('Usage ./028.py number')
    return 1    


  print(f(int(sys.argv[1])))

if __name__ == '__main__':
  main()