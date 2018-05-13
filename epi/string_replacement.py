#delete b, replace a with 2 d

def replace_string(s):
  a = list(s)
  write_idx, new_size = 0,0
  for i in range(len(s)):
    if a[i] == 'a':
      write_idx += 2
      a.append('  ')
    elif s[i] != 'b':
      write_idx += 1
  cur_idx = len(s) -1
  while cur_idx >=0:
    if a[cur_idx] == 'a':
      a[write_idx - 1] = 'd'
      a[write_idx - 2] = 'd'
      write_idx -= 2
      cur_idx -= 2
    elif a[cur_idx] != 'b':
      a[write_idx - 1] = a[cur_idx]
      cur_idx -= 1
      write_idx -= 1
    else:
      cur_idx -= 1
  return ''.join(a)

print replace_string('abacf')
print replace_string('acdbbca')
