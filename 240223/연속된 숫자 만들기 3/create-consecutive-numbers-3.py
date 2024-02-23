arr = list(map(int, input().split()))
# 양쪽 중에서 차이가 큰 쪽으로 이동
a = arr[1] - arr[0]
b = arr[2] - arr[1]
maxDiff = max(a, b)
print(maxDiff - 1)