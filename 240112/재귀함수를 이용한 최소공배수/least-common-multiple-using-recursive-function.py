n = int(input())
l = list(map(int, input().split()))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm_recursive(numbers, n):
    if n == 1:
        return numbers[0]
    else:
        return lcm(numbers[n - 1], find_lcm_recursive(numbers, n - 1))
result = find_lcm_recursive(l, n)
print(result)