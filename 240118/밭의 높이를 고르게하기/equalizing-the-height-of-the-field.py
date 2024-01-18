import sys
N, H, T = map(int, input().split())
l = list(map(int, input().split()))
min_cost = sys.maxsize 
for i in range(N-T+1):
    cost = 0
    for k in range(i, T+i):
        cost += abs(H - l[k])
    min_cost = min(min_cost, cost)
print(min_cost)