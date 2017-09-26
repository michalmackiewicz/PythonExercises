#!/usr/bin/python3

import sys

#Define a class which has at least two methods:
#getString: to get a string from class
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.

class MyString:
  def __init__(self, x):
  	self.x = x

  def getString(self):
    return self.x

  def printString(self):
    print(self.x.upper())


def main():
  if len(sys.argv) == 1:
    print ('Usage ./006.py string')
    return 1
    
  x = MyString(sys.argv[1])

  print(x.getString())

  x.printString()

if __name__ == '__main__':
  main()

