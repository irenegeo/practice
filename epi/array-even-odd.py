#reorder array even frist odd last
def even_odd(a):
  next_even = 0
  next_odd = len(a) -1
  while next_even < next_odd:
    if a[next_even] % 2 == 0:
      next_even +=1
    else:
      a[next_even], a[next_odd] = a[next_odd], a[next_even]
      next_odd -= 1
  return a

print even_odd([1,2,3,4,5,6])