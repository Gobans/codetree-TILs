def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def prime_sum(a, b):
    sum = 0
    for i in range(a, b+1):
        if is_prime(i):
            sum += i
    print(sum)
a, b = map(int, input().split())
prime_sum(a, b)