N = int(input())
board = []
for _ in range(N):
    l = list(map(int, input().split()))
    board.append(l)
max_cnt = 0
for i in range(N):
    cnt = 0
    for j in range(N-2):
        cnt = board[i][j] + board[i][j+1] + board[i][j+2]
    max_cnt = max(max_cnt, cnt)
print(max_cnt)