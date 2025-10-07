def special_pythagorean_triplet(total: int):
    for a in range(1, total):
        for b in range(a + 1, total - a):
            c = total - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None
result = special_pythagorean_triplet(1000)
print("Product of the Pythagorean triplet (a*b*c) for sum 1000:", result)