#!/usr/bin/python3

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def main():
  numbers = []

  for x in range(2000, 3200):
  	if x%5 > 0 and x%7 ==0:
  	  numbers.append(str(x))

  print(', '.join(numbers))

if __name__ == '__main__':
  main()
