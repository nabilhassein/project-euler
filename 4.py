# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def problem4():
  maxproduct = float("-inf")
  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i * j
      string = str(product)
      if product > maxproduct and string == string[::-1]:
        maxproduct = product
        result = string
  return result

print problem4()