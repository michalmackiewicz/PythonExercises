#!/usr/bin/python3


# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


def main():


  sentence = input()
  letters = 0
  digits = 0

  for x in sentence:
    if x.isalpha():
      letters+=1
    if x.isdigit():
      digits+=1
  
  print('LETTERS '+str(letters))
  print('DIGITS '+str(digits))


if __name__ == '__main__':
  main()

