def even_fibonacci_sum(limit: int):
    a, b = 1, 2  # First two Fibonacci numbers
    total = 0

    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b 

    return total



result = even_fibonacci_sum(4000000)
print("Sum of even Fibonacci numbers below 4 million:", result)