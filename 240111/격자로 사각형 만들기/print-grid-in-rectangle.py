n = int(input())
board = [ [ 0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    board[0][i] = 1
    board[i][0] = 1
for i in range(1, n):
    for j in range(1, n):
        board[i][j] = board[i-1][j] + board[i][j-1] + board[i-1][j-1]
for i in range(n):
    print(*board[i])