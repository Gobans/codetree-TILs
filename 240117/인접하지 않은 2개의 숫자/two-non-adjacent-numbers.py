n = int(input())
l = list(map(int, input().split()))
max_diff = 0
for i in range(n-2):
    for j in range(i+2, n):
        max_diff = max(max_diff, l[i] + l[j])
print(max_diff)