#2,3,5,5,7 > 2,3,5,7

def remove_duplicate(a):
  write_index=1
  for i in range(1,len(a)):

    if a[write_index - 1] != a[i]:
      a[write_index] = a[i]
      write_index+=1
  return a[:write_index]

print remove_duplicate([1,1,2,2])

# remove occurences

def remove_occurences(a, v):
  write_index = 0
  for i in range(0,len(a)):
    if a[i] != v:
      a[write_index] = a[i]
      write_index += 1
  return a[:write_index]

print remove_occurences([1,1,2,2], 1)
print remove_occurences([1,1,2,2], 2)