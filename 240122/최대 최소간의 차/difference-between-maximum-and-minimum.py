import sys
MAX_A = 10000

n, k = map(int, input().split())
li = list(map(int, input().split()))

# 최종적으로 나오는 수들 중 최대 최소간의 차가 k 이하가 되어야 함
# 수 a가 수 b로 바뀌는데 드는 비용이 |a - b|
# 필요한 최소 비용을 구하기

res = sys.maxsize

for i in range(1, MAX_A + 1):
    count = 0
    min_value = i
    max_value = i + k

    for elem in li:
        if elem < min_value:
            count += (min_value - elem)
        if elem > max_value:
            count += (elem - max_value)

    res = min(res, count)

print(res)