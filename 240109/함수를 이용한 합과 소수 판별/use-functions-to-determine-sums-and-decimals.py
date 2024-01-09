def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def is_digit_even(n):
    sum = 0
    while n%10 >= 1:
        sum += n%10
        n /= 10
    sum = int(sum)
    if sum%2 == 0:
        return True
    else:
        return False

def find_cnt(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_prime(i) and is_digit_even(i):
           cnt += 1
    return cnt

a, b = map(int, input().split())
print(find_cnt(a, b))