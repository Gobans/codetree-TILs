board = [[]]

def is_valid(i, j, color):
    # 가로 (오른쪽만 탐색해도 괜찮음)
    horizon_cnt = 0
    for k in range(j, i+5):
        if k <= 19 and board[i][k] == color:
            horizon_cnt += 1
        else:
            break
    if horizon_cnt == 5:
        return (i, j + 2)
    # 세로
    vertical_cnt = 0
    for k in range(i, i+5):
        if k <= 19 and board[k][j] == color:
            vertical_cnt += 1
        else:
            break
    if vertical_cnt == 5:
        return (i+2, j)
    
    # 우측하단 대각선
    right_diagonal_cnt = 0
    for k in range(5):
        if i+k <= 19 and j+k <= 19 and board[i+k][j+k] == color:
            right_diagonal_cnt += 1
        else:
            break
    if right_diagonal_cnt == 5:
        return (i+2, j+2)

    # 좌측하단 대각선
    left_diagonal_cnt = 0
    for k in range(0, -5, -1):
        if i-k <= 19 and j+k >= 1 and board[i-k][j+k] == color:
            left_diagonal_cnt += 1
        else:
            break
    if left_diagonal_cnt == 5:
        return (i+2, j-2)
    return (0, 0)

for _ in range(19):
    l = list(map(int, input().split()))
    board.append([0] + l)

result = 0
result_coordinate = (0, 0)

for i in range(1, 20):
    for j in range(1, 20):
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
if result != 0:
    print(result_coordinate[0], result_coordinate[1])