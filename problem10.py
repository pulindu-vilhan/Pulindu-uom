#Summation of Primes

def is_prime(n: int) :

    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_primes(limit: int) :
    total = 0
    for number in range(2, limit):
        if is_prime(number):
            total += number
    return total

result = sum_primes(2000000)
print("Sum of all primes below 2 million:", result)
