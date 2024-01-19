n, m = map(int, input().split())
l = [0] + list(map(int, input().split()))

# 움직임을 했을떄 원소값들의 합이 최대?
max_sum = 0
for i in range(1, n+1):
    m_sum = 0
    now_idx = i
    for j in range(m):
        now_idx = l[now_idx]
        m_sum += l[now_idx]
    max_sum = max(max_sum, m_sum)
print(max_sum)