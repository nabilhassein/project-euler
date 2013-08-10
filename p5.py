# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?

### END PROBLEM STATEMENT; BEGIN MY COMMENTARY

# My strategy is to create a list satisfying the following:
# if i is composite, list[i] == 0
# if i is prime, list[i] == the maximum multiplicity of the prime number i
#   in the prime factorization of any integer from 1 to n
# the answer is the product of all p^n where p is prime, n == list[p]

# based on https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation
def sieve(n):
  A = [False, False] + [True] * (n - 2)
  for i in range(2, int(n**0.5)):
    if A[i]:
      for j in range(i*i, n)[::i]:
        A[j] = False
  return [index for index, prime in enumerate(A) if prime]

# based on https://en.wikipedia.org/wiki/Trial_division#Method
def primeFactors(n):
  if n <= 1:
    return []
  factors = []
  primes  = sieve(1 + int(n**0.5))
  for p in primes:
    while n % p == 0:
      factors.append(p)
      n = n // p
  if n > 1:
    factors.append(n)
  return factors


def problem5(n):
  factorizations = [[]] * n
  for i in range(0, n):
    factorizations[i] = primeFactors(i)

  primes         = sieve(n)
  maxPrimeCounts = [0] * n
  for f in factorizations:
    for p in primes:
      maxPrimeCounts[p] = max(maxPrimeCounts[p], f.count(p))

  product = 1
  for prime, multiplicity in enumerate(maxPrimeCounts):
    if multiplicity > 0:
      product *= (prime**multiplicity)
  return product

print problem5(20)