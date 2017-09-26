#!/usr/bin/python3

#convert decimal number to binary string

def dec2bin(number):
  result = ''
  while number>0:
    result = str(number % 2) + result
    x = int(number / 2)
  return result

def main():

  print(dec2bin(130))

if __name__ == '__main__':
  main()

