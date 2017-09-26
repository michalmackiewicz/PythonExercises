#!/usr/bin/python3


#Write a program that accepts sequence of lines as input and prints the lines after making
# all characters in the sentence capitalized.
#Suppose the following input is supplied to the program:
#Hello world
#Practice makes perfect
#Then, the output should be:
#HELLO WORLD
#PRACTICE MAKES PERFECT


def main():
  print ("Enter text, press enter twice to end")
  texts = []
  x = ' '
  while True:
    x = input()
    if not x:
      break
    texts.append(x)

  for x in texts:
    print(x.upper())


if __name__ == '__main__':
  main()

