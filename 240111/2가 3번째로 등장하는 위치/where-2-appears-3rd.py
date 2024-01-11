n = int(input())
l = [0] + list(map(int, input().split()))
cnt = 0
for i in range(1,len(l) + 1):
    if l[i] == 2:
        cnt += 1
        if cnt == 3:
            print(i)
            break