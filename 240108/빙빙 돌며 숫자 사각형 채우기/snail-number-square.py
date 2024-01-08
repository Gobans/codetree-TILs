import sys
n, m = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(m)] for _ in range(n)]
board[0][0] = 1
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
nowDir = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

for i in range(2, n*m + 1):
    nx, ny = x + dx[nowDir], y + dy[nowDir]
    if not in_range(nx, ny) or board[nx][ny] != 0:
        nowDir = (nowDir + 1) % 4
    x, y = x + dx[nowDir], y + dy[nowDir]
    board[x][y] = i
for i in range(n):
    for j in range(m):
        print(board[i][j], end = ' ')
    print()