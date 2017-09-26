#!/usr/bin/python3

#Write a program that computes the net amount of a bank account based a transaction 
#log from console input. The transaction log format is shown as following:
#D 100
#W 200
#
#where D means deposit while W means withdrawal.


def main():
  print ("Enter transactions, press enter twice to end")
  amount = 0
  x = ' '
  while True:
    x = input()
    if not x:
      break
    transaction = x.split(' ')

    try:
      if transaction[0] == 'D':
        amount += int(transaction[1])

      elif transaction[0] == 'W':
        amount -= int(transaction[1])

      else:
        print("Unknown transaction")
    except ValueError:
      print ("Wrong numeric value: "+transaction[1])

  print(str(amount))

if __name__ == '__main__':
  main()

