#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
  max_profit = None
  
  for i in rage(0, len(prices)):
    #subtract each price to each one up price
    for j in rage(i+1, len(prices)):
      
    
  
  #Find the maximum difference between smallest n largest price in list of prices.
  #Max profit substracts price by another price that comes _before_ NOT after in the list of prices.

  #prices = -1
  #max profit = prices[before] - prices[after]
  
  # for i in range(len(prices) -1):
  #   for j in range(i + len(prices)):
  #     if prices[j] - prices[i] > profit:
  #       profit = prices[j] - prices[i]
  #      i+=1
  #     return profit
    
    #start at end of the array
    #set minimum price and max profit
    
    
    
print(find_max_profit([1500, 300, 8000, 250, 23, 11]))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))