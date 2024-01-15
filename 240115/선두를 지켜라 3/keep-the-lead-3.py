N, M = map(int, input().split())
AMove = []
BMove = []
for _ in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        AMove.append(v)
for _ in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        BMove.append(v)
nowA = 0
nowB = 0
honor = (0, 0)
tempHonor = (0, 0)
answer = 0
for a, b in zip(AMove, BMove):
    nowA += a
    nowB += b
    if nowA == nowB:
        tempHonor = (1, 1)
    elif nowA > nowB:
        tempHonor = (1, 0)
    else:
        tempHonor = (0, 1)
    if honor != tempHonor:
        answer += 1
        honor = tempHonor
print(answer)