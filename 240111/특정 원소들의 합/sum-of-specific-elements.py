sum = 0
for i in range(1, 5):
    line = list(map(int, input().split()))
    for j in range(i):
        sum += line[j]
print(sum)