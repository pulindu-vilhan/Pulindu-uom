from math import gcd

def lcm(a: int, b: int) :
    return a * b // gcd(a, b)

def smallest_multiple(limit: int) -> int:
    multiple = 1
    for i in range(1, limit + 1):
        multiple = lcm(multiple, i)
    return multiple

result = smallest_multiple(20)
print("Smallest multiple divisible by all numbers from 1 to 20:", result)
