# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from math import log

# based on https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation
def sieve(n):
  A = [False, False] + [True] * (n - 2)
  for i in range(2, int(n**0.5)):
    if A[i]:
      for j in range(i*i, n)[::i]:
        A[j] = False
  return [index for index, prime in enumerate(A) if prime]


def problem10(n):
  return sum(sieve(n))

print problem10(2000000)