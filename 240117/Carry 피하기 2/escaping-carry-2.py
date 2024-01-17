n = int(input())

def is_carry(a, b, c):
    ca, cb, cc = a, b, c
    while a > 0 or b > 0 or c > 0:
        a_digit = a % 10
        b_digit = b % 10
        c_digit = c % 10

        if a_digit + b_digit + c_digit > 10:
            return -1
        
        a //= 10
        b //= 10
        c //= 10
    return ca + cb + cc

l = []
max_sum = -1

for _ in range(n):
    l.append(int(input()))
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            max_sum = max(max_sum, is_carry(l[i], l[j], l[k]))
print(max_sum)