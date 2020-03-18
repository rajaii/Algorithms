#!/usr/bin/python

import argparse
#worked on most cases but did not account for all cases back to Understand
# def find_max_profit(prices):
#   is_neg = []
#   is_pos = []

#   max = 0
#   for i in range(0, len(prices) - 1):
#       max = 0
#       #account for negs and 0
#       if prices[i+1] - prices[i] < 0 or prices[i+1] - prices[i] == 0:
#         #skip all the folloowing if there are any positive values
#         if len(is_pos) <= 0:
#           #add to neg arr and check when all diffs are negs
#           is_neg.append(prices[i+1] - prices[i])
          
#           if len(is_neg) == len(prices) - 1:
#             highest_neg = 0
#             for j in range(0, len(is_neg) - 1):
#               for k in range(1, len(is_neg) - 1):
#                 if is_neg[j] == 0:
#                   max = 0
#                   break
#                 if is_neg[j] > is_neg[k]:
#                   highest_neg = is_neg[j]
#                   max = highest_neg
#             return max
#       #repeat with pos logic
#       elif prices[i+1] - prices[i] > 0:
#         is_pos.append(prices[i+1] - prices[i])
#         highest_pos = prices[i+1] - prices[i]
#         max = highest_pos
#         for j in range(0, len(is_pos) - 1):
#           for k in range(1, len(is_pos) - 1):
#             if is_pos[j] > is_pos[k]:
#               highest_pos = is_pos[j]
#               max = highest_pos
#         return max


def find_max_profit(prices):
  
  
  total_diffs = []
  for i in range(len(prices) -1):
    for j in range(i+1, len(prices) -1):
      diff = prices[j] - prices[i]
      total_diffs.append(diff)
  return max(total_diffs)
      # max = 0
      # diff = prices[j] - prices[i]
      # if diff < 0 or diff == 0:
      #   #skip all the folloowing if there are any positive values
      #   if len(is_pos) <= 0:
      #     #add to neg arr and check when all diffs are negs
      #     is_neg.append(diff)
      #     total_diffs.append(diff)
      #     if len(is_neg) == len(total_diffs):
      #       highest_neg = 0
      #       for k in range(0, len(is_neg) - 1):
      #         for l in range(1, len(is_neg) - 1):
      #           if is_neg[l] == 0:
      #             max = 0
      #             break
      #           if is_neg[l] > is_neg[k]:
      #             highest_neg = is_neg[l]
      #             max = highest_neg
      #         return max
       
      # elif prices[j] - prices[i] > 0:
      #   is_pos.append(diff)
      #   total_diffs.append(diff)
      #   highest_pos = 0
      #   for k in range(0, len(is_pos) - 1):
      #     for l in range(1, len(is_pos) - 1):
      #       if is_pos[l] > is_pos[k]:
      #         highest_pos = is_pos[l]
      #         max = highest_pos
      #     return max
    
    
    
  
  
p = [100, 90, 80, 50, 20, 10]
find_max_profit(p)

# if __name__ == '__main__':
#   # This is just some code to accept inputs from the command line
#   parser = argparse.ArgumentParser(description='Find max profit from prices.')
#   parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
#   args = parser.parse_args()

#   print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))