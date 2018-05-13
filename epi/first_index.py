def first_index(a,b):
  l = min(len(a), len(b))
  for i, item in enumerate(L):
    if a[i] != b[i]:
      return i

print first_index([1,1,2,2], [1,1,3])