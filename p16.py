# Power digit sum
# Problem 16

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

# What is the sum of the digits of the number 2^1000?

def sumOfDigits(n):
  return sum([int(c) for c in str(n)])

print sumOfDigits(2**1000)