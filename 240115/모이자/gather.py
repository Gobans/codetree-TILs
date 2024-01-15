import sys
n = int(input())
l = list(map(int, input().split()))
minMove = sys.maxsize
for i in range(n):
    move = 0
    for j in range(n):
        move += abs(i-j)*l[j]
    if move < minMove:
        minMove = move
print(minMove)