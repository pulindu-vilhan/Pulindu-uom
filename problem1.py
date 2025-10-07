def multiples_of_3_or_5(limit: int):
    total = 0
    for n in range(limit):
        if n % 3 == 0 or n % 5 == 0:
            total += n
    return total



result = multiples_of_3_or_5(1000)
print("Sum of multiples of 3 or 5 below 1000:", result)