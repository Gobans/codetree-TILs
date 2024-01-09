def power(a, b):
    sum = a
    for _ in range(b-1):
        sum = sum * a
    return sum
a, b = map(int, input().split())
print(power(a, b))