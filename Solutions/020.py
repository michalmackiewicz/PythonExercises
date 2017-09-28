#!/usr/bin/python3

import re
import math

# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

def main():
  print ("Enter list of steps, press enter twice to end")
  steps = []

  while True:
    s = input()
    if not s:
      break
    
    if re.search(r'^(UP|DOWN|LEFT|RIGHT) \d+$',s):
      steps.append(tuple(s.split(' ')))
    else:
      print ("Enter direction and number of steps separated by space.")

  x = 0
  y = 0
  for step in steps:
    if step[0] == 'UP': y += int(step[1])
    if step[0] == 'DOWN': y -= int(step[1])
    if step[0] == 'RIGHT': x += int(step[1])
    if step[0] == 'LEFT': x -= int(step[1])

  result = math.sqrt(x**2 + y**2)
  print (str(int(result)))

if __name__ == '__main__':
  main()

