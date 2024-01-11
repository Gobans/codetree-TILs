n = int(input())
num = 1
board = [ [0 for _ in range(n)] for _ in range(n)]
# True: up False: down
direction = True
for i in range(n-1,-1, -1):
    if direction:
        for j in range(n-1, -1, -1):
            board[j][i] = num
            num += 1
    else:
        for j in range(n):
            board[j][i] = num
            num += 1
    direction = not direction
for i in range(n):
    print(*board[i])