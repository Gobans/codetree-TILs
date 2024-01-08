def gcd(n, m):
    if (m == 0):
        return n
    return gcd(m, n%m)

def min_multiple(n, m):
    if n > m:
        g = gcd(n, m)
    else:
        g = gcd(m, n)
    return (n*m)/g
n, m = map(int, input().split())
print(int(min_multiple(n, m)))