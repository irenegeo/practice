#a[0]<=a[1]>=a[2]<=a[3]

def rearrange(a):
  for i in range(len(a) - 1):
    a[i:i+2] = sorted(a[i:i+2], reverse = i%2)
  return a

a = [1,2,3,4,5,6]
print rearrange(a)

a = [1,2,3,4,5,6, 7]
print rearrange(a)