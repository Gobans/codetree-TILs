n, m = map(int, input().split())
board = [ [ 0 for _ in range(m)] for _ in range(n)]
for _ in range(m):
    r, c = map(int, input().split())
    board[r-1][c-1] = r*c
for i in range(n):
    print(*board[i])