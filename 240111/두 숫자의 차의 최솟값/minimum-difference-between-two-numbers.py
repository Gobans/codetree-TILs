n = int(input())
l = list(map(int, input().split()))
minDiff = 100
for i in range(len(l)):
    for j in range(i+1, len(l)):
        diff = l[j] - l[i]
        if diff < minDiff:
            minDiff = diff
print(minDiff)