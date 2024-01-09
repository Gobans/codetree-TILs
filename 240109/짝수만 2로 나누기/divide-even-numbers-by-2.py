N = int(input())
l = list(map(int, input().split()))
def change_even(l):
    for idx, i in enumerate(l):
        if i%2 == 0:
            l[idx] = int(l[idx] / 2)
change_even(l)
print(*l)