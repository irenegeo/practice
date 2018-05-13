import string
def string_to_int(s):
  num = 0
  if s.startswith("-"):
    is_negative = True
    s = s[1:]
  else:
    is_negative = False

  for c in s:
    num *= 10
    num += string.digits.index(c)
  if is_negative:
    num = (-1) * num
  return num


print string_to_int("1233")
print string_to_int("-10")
print string_to_int("-1")


def str_to_int(s):
  # if s[0] == '-':
  #   is_negative = True
  #   s = s[1:]
  # else:
  #   is_negative = False
  print s
  num = reduce(lambda running_sum, c:
               running_sum*10 + string.digits.index(c),
               s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)
  return num

  # if is_negative:
  #   return (-1) * num
  # else:
  #   return num

print str_to_int("1233")
print str_to_int("-10")
print str_to_int("-1")

def int_to_str(num):
  negative  = False
  if num < 0:
    num = -1 * num
    negative = True
  s = []
  while True:
    s.append(chr(ord('0') + num%10))
    num = num/10
    if num == 0:
      break

  return ('-' if negative else '') + ''.join(reversed(s))

print int_to_str(123)
print int_to_str(-123)

def col_to_int(s):
  num = 0
  for c in s:
    num *= 26
    num += ord(c) - ord("A") +1
  return num
print "AAA"
print col_to_int("AA")
print col_to_int("AB")