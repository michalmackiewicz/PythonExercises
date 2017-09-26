#!/usr/bin/python3

#convert decimal number to binary string

def dec2bin(x):
  result = ''
  while x>0:
    result = str(x%2) + result
    x = int(x / 2)
  return result

def main():

  print(dec2bin(130))

if __name__ == '__main__':
  main()

