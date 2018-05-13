def find_max_substring(s):
    usec = set()
    max_len = 0
    for i in xrange(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_unique(s[i:j]) and j - i > max_len:
                max_len = j - i
    print max_len


def is_unique(astring):
    us = set()
    for letter in astring:
        if letter not in us:
            us.add(letter)
        else:
            return False
    return True

def sliding_wind(s):
    unique_set = set()
    i = 0
    j = 0
    max_length = 0
    while i < len(s) and j < len(s):
        if s[j] not in unique_set:
            unique_set.add(s[j])
            j = j + 1
            max_length = max(max_length, j - i)
        else:
            unique_set.remove(s[i])
            i = i + 1
    return max_length, unique_set

"""

"""

def sliding_wind_dict(s):
    # current index of character
    unique_dict = {}
    i = 0
    max_len = 0
    for j in xrange(len(s)):
        print unique_dict
        print s[j]
        if s[j] in unique_dict:
            i = max(unique_dict[s[j]], i)
        max_len = max(max_len, j -i +1)
        unique_dict[s[j]] = j + 1

#Find longest unique - wrong
def find_uniq_substr(s):
    res = ''
    max = 1
    for c in s:
        if c in res:
            if max < len(res):
                max = len(res)
            res = c
        else:
            res += c
    return max

# Find length of longest repeating char
def find_max_repeating(s):
    res = s[0]
    max_len=1
    for c in s[1:]:
        if c in res:
            res +=c
            max_len = max(max_len, len(res))
            # if max_len < len(res):
            #     max_len = len(res)
        else:
            res = c
    return max_len

def max_repeating(s):
    maxsofar = 1
    i = 0
    while i < len(s):
      cnt = 1
      while i + 1 < len(s) and s[i] == s[i+1]:
          cnt += 1
          i += 1
      maxsofar = max(maxsofar, cnt)
      i += 1
    return maxsofar
# print sliding_wind_dict("abbc")
print find_uniq_substr("aaa")
print find_uniq_substr("dfghjopdabbc")
print find_max_repeating("abbc")
# print sliding_wind_dict("abcda")
print sliding_wind("abbcdeb")
print sliding_wind("abacd")
print find_uniq_substr("abacd")