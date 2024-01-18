import sys
N, S = map(int, input().split())
l = list(map(int, input().split()))

min_diff = sys.maxsize
l_sum = sum(l)
for i in range(N-1):
    for j in range(i+1, N):
        # if abs(S - (l[i] + l[j])) < min_diff:
        #     min_diff_sum = 
        min_diff = min(min_diff, abs(S - ( l_sum - (l[i] + l[j]))))
print(min_diff)