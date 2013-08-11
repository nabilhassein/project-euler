# 10001st prime
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?

from math import log

# based on https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Implementation
def sieve(n):
  A = [False, False] + [True] * (n - 2)
  for i in range(2, int(n**0.5)):
    if A[i]:
      for j in range(i*i, n)[::i]:
        A[j] = False
  return [number for number, isPrime in enumerate(A) if isPrime]


# for origin of 'bound', see
# https://en.wikipedia.org/wiki/Prime_number_theorem#Approximations_for_the_nth_prime_number
def problem7(n):
  bound  = int(n*log(n) + n*log(log(n)))
  primes = ["dummy for index zero"] + sieve(bound)
  return primes[n]

print problem7(10001)