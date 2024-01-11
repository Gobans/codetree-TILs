l = list(map(int, input().split()))
for i in range(len(l)):
    if l[i]%3 == 0:
        print(l[i-1])
        break