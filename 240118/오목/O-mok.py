board = [[]]

def is_valid(i, j, color):
    # 가로 (오른쪽만 탐색해도 괜찮음)
    horizon_cnt = 0
    for k in range(j, i+5):
        if i <= 19 and board[i][k] == color:
            horizon_cnt += 1
        else:
            break
    if horizon_cnt == 5:
        return (i, j + 2)
    
    # 대각선
    diagonal_cnt = 0
    for k in range(5):
        if i+k <= 19 and j+k <= 19 and board[i+k][j+k] == color:
            diagonal_cnt += 1
        else:
            break
    if diagonal_cnt == 5:
        return (i+2, j+2)
    return (0, 0)

for _ in range(19):
    l = list(map(int, input().split()))
    board.append([0] + l)

result = 0
result_coordinate = (0, 0)

for i in range(1, 19):
    for j in range(1, 19):
        if board[i][j] != 0:
            result_coordinate = is_valid(i, j, board[i][j])
            if result_coordinate != (0, 0):
                result = board[i][j]
                break
        if result_coordinate != (0, 0):
            break
    if result_coordinate != (0, 0):
        break


print(result)
print(result_coordinate[0], result_coordinate[1])