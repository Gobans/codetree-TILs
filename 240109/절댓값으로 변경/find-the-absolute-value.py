N = int(input())
l = list(map(int, input().split()))
def print_absolute(n):
    if n < 0:
        n = -n
    print(n, end = ' ')
for i in l:
    print_absolute(i)