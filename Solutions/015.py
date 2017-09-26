#!/usr/bin/python3

import sys
import re

#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
#Suppose the following input is supplied to the program:
#9
#Then, the output should be:
#11106

def main():
  if len(sys.argv) != 2 or not re.search(r'^\d$',sys.argv[1]):
    print ('Usage ./015.py digit')
    return 1
    
  digit = int(sys.argv[1])

  result = digit + digit*10 + digit + digit*100 + digit*10 + digit + digit*1000 + digit*100 + digit*10 + digit

  print(str(result))

 
if __name__ == '__main__':
  main()

