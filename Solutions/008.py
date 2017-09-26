#!/usr/bin/python3

import sys
import re

#Write a program which takes 2 digits, X Y as input and generates a 2-dimensional array. 
#The element value in the i-th row and j-th column of the array should be i*j.
#Note: i=0,1.., X-1; j=0,1,¡­Y-1.
#Example
#Suppose the following inputs are given to the program:
#3 5
#Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 




def main():
  if len(sys.argv) != 3 or not re.search(r'^\d+$',sys.argv[1]) or not re.search(r'^\d+$',sys.argv[2]):
    print ('Usage ./008.py number1 number2')
    return 1
    
  columns = int(sys.argv[2])
  rows = int(sys.argv[1])

  result = [[column*row for column in range(columns)] for row in range(rows)] 

  print(result)

 
if __name__ == '__main__':
  main()

