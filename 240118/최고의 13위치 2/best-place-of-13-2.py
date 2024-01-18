N = int(input())
boards = []
for _ in range(N):
    l = list(map(int, input().split()))
    boards.append(l)
max_cnt = 0
for i in range(N):
    for j in range(N-2):
        cnt = boards[i][j] + boards[i][j+1] + boards[i][j+2]
        # 같은 행
        for k in range(j+3, N-2):
            temp_cnt = boards[i][k] + boards[i][k+1] + boards[i][k+2]
            max_cnt = max(max_cnt, cnt + temp_cnt)
        # 다른 행
        for l in range(i+1, N):
            for k in range(N-2):
                temp_cnt = boards[l][k] + boards[l][k+1] + boards[l][k+2]
                max_cnt = max(max_cnt, cnt + temp_cnt)
print(max_cnt)