def plus_one(a):
  a[-1] +=1
  for i in reversed(range(1, len(a))):
    if a[i] != 10:
      break
    a[i] = 0
    a[i -1] += 1
  print a
  if a[0] == 10:
    a[0] = 1
    a.append(0)
  return a

a = [9,9]
print plus_one(a)

# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.