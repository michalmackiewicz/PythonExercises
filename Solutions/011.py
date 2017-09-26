#!/usr/bin/python3

import sys

#Write a program which accepts a sequence of comma separated 4 digit binary numbers
# as its input and then check whether they are divisible by 5 or not. 
#The numbers that are divisible by 5 are to be printed in a comma separated sequence.
#Example:
#0100,0011,1010,1001
#Then the output should be:
#1010

def main():
  if len(sys.argv) == 1:
    print ('Usage ./011.py words comma-separated')
    return 1
    
  words = sys.argv[1].split(',') 
  words = set(words)

  print(' '.join(sorted(words)))

if __name__ == '__main__':
  main()

