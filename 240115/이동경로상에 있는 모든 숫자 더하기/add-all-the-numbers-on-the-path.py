N, T = map(int, input().split())
command = input()
board = [[]]
for _ in range(N):
    line = [0] + list(map(int, input().split()))
    board.append(line)
mid =  N // 2 + 1
x, y = mid, mid
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
now_direction = 0
sum = board[y][x]
for c in command:
    if c == "L":
        now_direction -= 1
        if now_direction == -1:
            now_direction = 3
    elif c == "R":
        now_direction = (now_direction + 1) % 4
    else:
        mx, my = x + dx[now_direction] , y + dy[now_direction]
        if mx >= 1 and mx <= N and my >= 1 and my <= N:
            sum += board[my][mx]
            x, y = mx, my
print(sum)