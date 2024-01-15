n, t = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
maxCnt = 0
for num in l:
    if num > t:
        cnt += 1
        if cnt > maxCnt:
            maxCnt = cnt
    else:
        cnt = 0
print(maxCnt)