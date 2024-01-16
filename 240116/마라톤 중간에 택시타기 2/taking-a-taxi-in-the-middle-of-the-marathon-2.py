# 1. 구간 (1, 2) (2, 3) 의 거리 구하기
# 2. 제거 했을때 구간의 거리 구하기.
# 3. 비교했을때 가장 큰 곳을 제거

n = int(input())
section_sum = []
coordinates = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))
# 구간별 거리 구하기
for i in range(n-1):
    now_x, now_y = coordinates[i][0], coordinates[i][1]
    next_x, next_y = coordinates[i+1][0], coordinates[i+1][1]
    s = abs(now_x - next_x) + abs(now_y - next_y)
    section_sum.append(s)
s_sum = sum(section_sum)
min_sum = sum(section_sum)

# 제거 했을떄 구간의 거리 구하기
for i in range(1, n-1):
    pre_x, pre_y = coordinates[i-1][0], coordinates[i-1][1]
    next_x, next_y = coordinates[i+1][0], coordinates[i+1][1]
    deleted_diff = abs(pre_x - next_x) + abs(pre_y - next_y)
    if deleted_diff < section_sum[i-1] + section_sum[i]:
        min_sum = min(min_sum, s_sum - (section_sum[i-1] + section_sum[i]) + deleted_diff)
print(min_sum)