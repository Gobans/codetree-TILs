N = int(input())
cows = list(map(int, input().split()))
cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if cows[i] <= cows[j] and cows[j] <= cows[k]:
                cnt += 1
print(cnt)