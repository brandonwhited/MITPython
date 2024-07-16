def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_primes_less_than_1000():
    sum_of_primes = 0
    for num in range(3, 1000, 2):  # Start from 3 and iterate over odd numbers
        if is_prime(num):
            sum_of_primes += num
    return sum_of_primes

result = sum_primes_less_than_1000()
print(f"The sum of prime numbers greater than 2 and less than 1000 is: {result}")
