# Project Euler Problem 7: 10001st Prime

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n: int) -> int:
    count = 0  # Count of primes found
    num = 2    # Number to check
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

result = nth_prime(10001)
print("The 10001st prime number is:", result)
