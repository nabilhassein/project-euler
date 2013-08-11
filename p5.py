# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?


# based on https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation
def sieve(n):
  A = [False, False] + [True] * (n - 2)
  for i in range(2, int(n**0.5)):
    if A[i]:
      for j in range(i*i, n)[::i]:
        A[j] = False
  return [number for number, isPrime in enumerate(A) if isPrime]

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
  primes          = sieve(n)
  maxMultiplicity = [0] * n
  for i in range(0, n):
    for p in primes:
      maxMultiplicity[p] = max(maxMultiplicity[p], primeFactors(i).count(p))

  product = 1
  for k, multiplicity in enumerate(maxMultiplicity):
    product *= k**multiplicity
  return product

print problem5(20)