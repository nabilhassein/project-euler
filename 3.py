# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

### END PROBLEM STATEMENT; BEGIN MY COMMENTARY

# This is the first result I found by searching the Web via Google for
# "factor prime number python": 
# http://stackoverflow.com/questions/15347174/python-finding-prime-factors
# It was so short that I had already internalized it by the time I could think
# to look away, and it was so elegant that it was pointless to try to write
# another solution. So I merely altered it slightly.
# The other solutions are my original work,
# except where noted (nowhere other than here at the time of writing).

def problem3(n):
  i = 2
  while i * i < n:
    while n % i == 0:
      n = n / i
    i = i + 1
  return n

print problem3(600851475143)