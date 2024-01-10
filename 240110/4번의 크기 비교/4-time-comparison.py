a = int(input())
l = list(map(int, input().split()))
for i in l:
    if a > i:
        print("1")
    else:
        print("0")