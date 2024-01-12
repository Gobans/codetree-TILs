def gcd(n, m):
    if m == 0:
        return n
    return gcd(m, n%m)
n = int(input())
l = list(map(int, input().split()))
def find_min(k):
    find = True
    for i in l:
        if k%i != 0:
            find_min(k+1)
            find = False
            break
    if find:
        print(k)
find_min(1)