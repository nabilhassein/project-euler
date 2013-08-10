# Special Pythagorean triplet
# Problem 9

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

### END PROBLEM STATEMENT; BEGIN MY COMMENTARY

# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
# states for all integers m, n s.t. m > n, a pythagorean triplet is given by
# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2

# so find m > n s.t. (m^2 - n^2) + 2mn + (m^2 + n^2) == 1000
# i.e.               2m^2 + 2mn == 1000
# i.e.               2m(m + n)  == 1000
def pair(k):
  for m in range(0, k):
    for n in range(0, m):
      if 2*m*(m+n) == k:
        return m, n

def problem9(k):
  m, n = pair(k)
  a = m**2 - n**2
  b = 2*m*n
  c = m**2 + n**2
  return a*b*c

print problem9(1000)