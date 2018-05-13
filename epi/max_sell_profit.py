# optimally buy and sell a stock
def max_profit(a):
  max_profit_so_far, min_price_so_far = 0.0, float('inf')
  for item in a:
    min_price_so_far = min(min_price_so_far, item)
    max_profit_so_far = max(max_profit_so_far, item - min_price_so_far)
  return max_profit_so_far

print "max profit"
print max_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])

# max_subarray
def equal_subarray(a):
  c = a[0]
  max_len = 0
  cur_len = 0
  for item in a:
    if c == item:
      cur_len +=1
      max_len = max(max_len, cur_len)
    else:
      cur_len = 0
      c = item
  return max_len * [c]

def max_double_profit(a):
  print a
  max_total_profit = 0.0
  min_price_so_far = float('inf')
  max_profit_first_pass = [0.0] * len(a)
  min_price_so_far = [float('inf')] * len(a)
  for i, price  in enumerate(a):
    min_price_so_far = min(min_price_so_far, price)
    max_total_profit = max(max_total_profit, price - min_price_so_far)
    max_profit_first_pass[i] = max_total_profit
  print max_profit_first_pass
  max_price_so_far = float('-inf')
  for i, price in enumerate(reversed(a[1:]), 1):
    max_price_so_far = max(max_price_so_far, price)
    max_total_profit = max(max_total_profit,
                           max_price_so_far - price + max_profit_first_pass[i - 1])

  return max_total_profit
print "max double profit"
print max_double_profit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250])