#!/usr/bin/python3

import sys
import re

# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to 
# print the company name of a given email address. Both user names and company names are composed of letters only.
# Example:
# If the following email address is given as input to the program:
# john@google.com
# Then, the output of the program should be:
# google

def main():
  if len(sys.argv) == 1:
    print ('Usage ./026.py email')
    return 1
    
  result = re.search(r'^\w+@(\w+)\.\w+$',sys.argv[1])

  if result: 
    print(result.group(1))

if __name__ == '__main__':
  main()

