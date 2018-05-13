def is_prime(n):
  is_prime = [0, 0] + (n+1)*[1]
  primes = []
  for i in range(2, n+1):
    if is_prime[i]:
      primes.append(i)
      for j in range(i, n+1, i):
        is_prime[j]= 0
  return primes

print is_prime(10)