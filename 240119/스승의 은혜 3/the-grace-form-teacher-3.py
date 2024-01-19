# N명의 학생에게 B만큼의 예산 선물.
# 가격과 배송비 합을 정렬

presents = []
N, B = map(int, input().split())
all_sum = 0
for _ in range(N):
    p, s = map(int, input().split())
    presents.append((p, s))
    all_sum += p + s
presents.sort(reverse = True, key = lambda x: x[0] + x[1])
max_cnt = 0
for i in range(N):
    c_sum = all_sum - ( presents[i][0] // 2 )
    # 빼보기
    cnt = N
    for j in range(N):
        if c_sum <= B:
                break
        if j != i:
            c_sum -= presents[j][0] + presents[j][1]
            cnt -= 1
    if c_sum <= B:
        max_cnt = max(max_cnt, cnt)
print(max_cnt)