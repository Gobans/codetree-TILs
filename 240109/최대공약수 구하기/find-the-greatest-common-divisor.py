def gcd(n, m):
    if (m == 0):
        return n
    return gcd(m, n%m)
n, m = map(int, input().split())
print(gcd(n, m))