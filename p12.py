# Highly divisible triangular number
# Problem 12

# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?

from operator import mul

def product(xs):
  return reduce(mul, xs, 1)

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

# from the link below, I used the quoted formula, but didn't look at the code:
# http://stackoverflow.com/questions/2844703/algorithm-to-find-the-factors-of-a-given-number-shortest-method
# "If n = p1^e1 * p2^e2 * ... * pk^ek, where each p is a prime number,
# then the number of factors of n is (e1 + 1)*(e2 + 1)* ... *(ek + 1)."
def divisorCount(n):
  factors = primeFactors(n)
  if not factors: return 0
  
  multiplicities = [0] * (1 + max(factors))
  for f in factors:
    multiplicities[f] += 1
  return product(map(lambda x: x + 1, multiplicities))

def trianglenumbers():
  i = 2
  while True:
    yield sum(range(1, i))
    i += 1

def problem12(bound):
  for n in trianglenumbers():
    if divisorCount(n) > bound:
      return n

print problem12(500)