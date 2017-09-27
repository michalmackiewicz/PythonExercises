#!/usr/bin/python3

import sys
import re

#A website requires the users to input username and password to register. Write a program to check 
#the validity of password input by users.
#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#3. At least 1 letter between [A-Z]
#4. At least 1 character from [$#@]
#5. Minimum length of transaction password: 6
#6. Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
#Passwords that match the criteria are to be printed, each separated by a comma.
#Example
#If the following passwords are given as input to the program:
#ABd1234@1,aF1#,2w3E*,2We3345
#Then, the output of the program should be:
#ABd1234@1


def main():
  if len(sys.argv) == 1:
    print ('Usage ./018.py comma-separated passwords')
    return 1
  
  results = []
  for password in sys.argv[1].split(','):
    if re.search(r'[a-z]',password) and re.search(r'[0-9]',password) and re.search(r'[A-Z]',password) and re.search(r'[$#@]',password) and len(password) >= 6 and len(password) <= 12:
      results.append(password)    	
  
  print(','.join(results))


if __name__ == '__main__':
  main()

