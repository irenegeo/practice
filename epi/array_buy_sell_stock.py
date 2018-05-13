# buy and sell stock for max profit

def buy_sell(prices):
  min_price_so_far, max_profit = float('inf'), 0
  for price in prices:
    max_profit_today = price - min_price_so_far
    max_profit = max(max_profit, max_profit_today)
    min_price_so_far = min(min_price_so_far, price)
  return max_profit

# buy sell twice
def buy_sell_twice(prices):
  min_price_so_far, max_profit = float('inf'), 0
  profits = [0] * len(prices)
  for i in range(len(prices)):
    max_profit_today = prices[i] - min_price_so_far
    max_profit = max(max_profit, max_profit_today)
    min_price_so_far = min(min_price_so_far, prices[i])
    profits[i] = max_profit
  max_price_so_far = float('-inf')
  max_total_profit = 0
  for i, price in reversed(list(enumerate(prices[1:], 1))):
    max_price_so_far = max(max_price_so_far, price)
    max_total_profit = max(max_price_so_far - price + profits[i-1], max_total_profit)
  return max_total_profit

prices = [12,11,13,9,12,8,14,13,15]
print buy_sell(prices)
print buy_sell_twice(prices)