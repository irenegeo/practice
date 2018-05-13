def is_palindrome(s):
  return all(s[i] == s[~i] for i in range(len(s)/2))


print is_palindrome("aba")
print is_palindrome("abba")