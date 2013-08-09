def problem4():
  maxproduct = float("-inf")
  for i in range(0, 1000):
    for j in range(0, 1000):
      product = i * j
      string = str(product)
      if product > maxproduct and string == string[::-1]:
        maxproduct = product
        result = string
  return result

print problem4()