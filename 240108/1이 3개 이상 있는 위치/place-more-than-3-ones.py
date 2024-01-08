import sys
n = int(sys.stdin.readline())
board = []
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    board.append(line)

def in_range(x, y):
    return x >= 0 and x < n and y >=0 and y < n

dys = [1, -1, 0, 0]
dxs = [0, 0, -1, 1]
answer = 0

for x in range(n):
    for y in range(n):
        num_cnt = 0
        for dx, dy in zip(dxs, dys):
            mx = x + dx
            my = y + dy
            if in_range(mx, my) and board[my][mx] == 1:
                num_cnt += 1
        if num_cnt >= 3:
            answer += 1
print(answer)