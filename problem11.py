# Problem 11: Largest product in a grid
grid = [
]

def largest_grid_product(grid, n=4):
    max_product = 0
    for i in range(20):
        for j in range(20):
            # horizontal
            if j + n <= 20:
                h = 1
                for k in range(n):
                    h *= grid[i][j+k]
                max_product = max(max_product, h)
            # vertical
            if i + n <= 20:
                v = 1
                for k in range(n):
                    v *= grid[i+k][j]
                max_product = max(max_product, v)
            # diagonal down-right
            if i + n <= 20 and j + n <= 20:
                dr = 1
                for k in range(n):
                    dr *= grid[i+k][j+k]
                max_product = max(max_product, dr)
            # diagonal up-right
            if i - n >= -1 and j + n <= 20:
                ur = 1
                for k in range(n):
                    ur *= grid[i-k][j+k]
                max_product = max(max_product, ur)
    return max_product

print(largest_grid_product(grid))

