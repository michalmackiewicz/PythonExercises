#!/usr/bin/python3

# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half 
# values in one line and the last half values in one line. 
# Use [n1:n2] notation to get a slice from a tuple.

def main():
  x = input()

  middle = int(len(x)/2)

  print(x[:middle])
  print(x[middle:])

if __name__ == '__main__':
  main()

