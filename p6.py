# Sum square difference
# Problem 6

# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one
# hundred natural numbers and the square of the sum.

def sumOfSquares(n):
  return sum([i**2 for i in range(1, n+1)])

def squareOfSum(n):
  return sum([i for i in range(1, n+1)]) ** 2

def problem6(n):
  return squareOfSum(n) - sumOfSquares(n)

print problem6(100)