#!/usr/bin/python3

import math

# Define a class named Shape and its subclass Square. The Square class has an init function which takes
# a length as argument. Both classes have a area function which can print the area of the shape where 
# Shape's area is 0 by default.
# To override a method in super class, we can define a method with the same name in the super class.

class Shape:
  """docstring for Shape"""
  def __init__(self):
    pass
  def getArea(self):
    return 0
		
class Sqare(Shape):
  def __init__(self, width):
  	self.w = width
  def getArea(self):
  	return self.w**2

class Circle:
	def __init__(self, radius):
		self.r = radius
	def getArea(self):
		area = math.pi * self.r**2
		return area

def main():
  x = Sqare(10)

  print(str(x.getArea()))

if __name__ == '__main__':
  main()

