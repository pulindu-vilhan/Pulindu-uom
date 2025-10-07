#Sum Square Difference

def sum_square_difference(n: int):
    
    # Sum of first n numbers
    total_sum = sum(range(1, n + 1))
    
    # Square of the sum
    square_of_sum = total_sum ** 2
    
    # Sum of the squares
    sum_of_squares = sum(i ** 2 for i in range(1, n + 1))
    
    # Difference
    difference = square_of_sum - sum_of_squares
    return difference

result = sum_square_difference(100)
print("Difference between square of sum and sum of squares for first 100 numbers:", result)
