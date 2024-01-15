N, S = map(int, input().split())
l = list(map(int, input().split()))
# N-2 조합의 합.
stack = [([], 0)]
minDiff = 10001
while stack:
    now = stack.pop()
    if len(now[0]) == N-2:
        diff = abs( sum(now[0]) - S)
        if diff < minDiff:
            minDiff = diff
        continue
    if now[1] == len(l):
        continue
    stack.append((now[0] , now[1] + 1))
    stack.append((now[0] + [l[now[1]]], now[1] + 1))
print(minDiff)