n = int(input())
board = [ [ 0 for _ in range(201)] for _ in range(201)]

def adjust_coordinate(n):
    return n + 100

for k in range(1, n+1):
    x1, y1, x2, y2 = map(adjust_coordinate, map(int, input().split()))
    for i in range(y1, y2):
        for j in range(x1, x2):
            if k%2 == 1:
                board[i][j] = 1
            else:
                board[i][j] = 2
cnt = 0
for i in range(201):
    for j in range(201):
        if board[i][j] == 2:
            cnt += 1
print(cnt)