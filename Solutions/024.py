#!/usr/bin/python3

import math

# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
# Use def methodName(self) to define a method.

class Circle:
	def __init__(self, radius):
		self.r = radius
	def getArea(self):
		area = math.pi * self.r**2
		return area

def main():
  x = Circle(10)

  print(str(x.getArea()))

if __name__ == '__main__':
  main()

