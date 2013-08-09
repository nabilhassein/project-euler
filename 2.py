def problem2():
  sum = 0
  prev, cur = 0, 1
  while prev < 4000000:
    prev, cur = cur, prev + cur
    if cur % 2 == 0:
      sum += cur
  return sum

print problem2()