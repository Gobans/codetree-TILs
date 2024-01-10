n = int(input())
divideNum = 1
cnt = 0
while n > 1:
    n /= divideNum
    divideNum += 1
    cnt += 1
print(cnt)