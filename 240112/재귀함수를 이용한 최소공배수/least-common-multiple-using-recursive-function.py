n = int(input())
l = list(map(int, input().split()))
def find_min(k):
    find = True
    for i in l:
        if k%i != 0:
            find = False
            break
    if find:
        print(k)
    else:
        find_min(k+1)
find_min(max(l))