#!/usr/bin/python3

#Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No". 

def main():
  x = input()

  if x.upper() == "YES":
    print("Yes")
  else:
  	print("No")

if __name__ == '__main__':
  main()

