n, m = map(int, input().split())
def change_num(a, b):
    a, b = b, a
    return a, b
n, m = change_num(n, m)
print(n, m)