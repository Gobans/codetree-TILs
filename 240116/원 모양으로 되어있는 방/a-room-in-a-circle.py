import sys
n = int(input())
rooms = []
rooms_sum = 0
for _ in range(n):
    p = int(input())
    rooms.append(p)
    rooms_sum += p
min_dist = sys.maxsize

for i in range(n):
    r = rooms_sum
    dist = 0
    dist_sum = 0
    for j in range(i, n):
        dist_sum += rooms[j] * dist
        r -= rooms[j]
        dist += 1
        if r <= 0:
            break
    if r >= 1:
        for j in range(i):
            dist_sum += rooms[j] * dist
            r -= rooms[j]
            dist += 1
            if r <= 0:
                break
    min_dist = min(min_dist, dist_sum)
print(min_dist)