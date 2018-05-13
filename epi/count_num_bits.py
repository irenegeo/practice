# Count num ibts set to 1 in a positive integer
def count_bits(x):
  num_bits = 0
  while x:
    num_bits += x & 1
    x >>= 1
  return num_bits

print count_bits(6)
print count_bits(7)
print count_bits(8)