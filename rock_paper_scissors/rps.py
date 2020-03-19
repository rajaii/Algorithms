#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  initial = ['rock', 'paper', 'scissors']
  ret_list = []
  

  for i in range(len(initial) - 1):
    for j in range(len(initial) - 1):
      ret_list.append([i])

  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')