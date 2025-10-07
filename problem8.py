def largest_product_in_series(n_digits: int):
    max_product = 0
    for i in range(len(number) - n_digits + 1):
        product = 1
        for j in range(n_digits):
            product *= int(number[i + j])
        if product > max_product:
            max_product = product
    return max_product
number = input("Enter the number: ").strip()
result = largest_product_in_series(13)
print("Largest product of 13 adjacent digits:", result)