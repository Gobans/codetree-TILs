a = input()
b = input()
maxCnt = len(a) + 1
cnt = 0
while True:
    if maxCnt == cnt:
        print("-1")
        break
    if a == b:
        print(cnt)
        break
    else:
        a = a[-1] + a[:-1]
        cnt += 1