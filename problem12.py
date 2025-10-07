def num_divisors(n):
    count = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            count += 2 if i != n//i else 1
    return count

n = 1
tri = 1
while num_divisors(tri) <= 500:
    n += 1
    tri += n

print(tri)