#!/usr/bin/python3

import sys
import re
import math

#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24
#
#If the output received is in decimal form, it should be rounded off to its nearest value 
#(for example, if the output received is 26.0, it should be printed as 26)

def q(d):
  c=50
  h=30
  return int(round(math.sqrt((2*c*d)/h)))

def main():
  if len(sys.argv) == 1 or not re.search(r'^(\d+(\.\d+)?,)*\d+(\.\d+)?$',sys.argv[1]):
    print ('Usage ./007.py numbers comma separated')
    return 1
    
  arguments = sys.argv[1].split(',') 

  results = []
  for x in arguments:
  	xf = float(x)
  	results.append(str(q(xf)))


  print(','.join(results))

 
if __name__ == '__main__':
  main()

