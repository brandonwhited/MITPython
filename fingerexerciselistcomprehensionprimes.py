# To get primes

# primes = [x for x in range(2, 100) if all(x % y != 0  for y in range(3, x))]
# print(primes)

non_primes = [x for x in range(2, 100) if not all(x % y != 0 for y in range(2, x))]
print(non_primes)

