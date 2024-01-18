board = [[]]
N, M = map(int, input().split())

def is_valid(i, j):
    # 가로 (오른쪽만 탐색해도 괜찮음)
    cnt = 0
    s = ""
    target = "LEE"
    for k in range(j, j+3):
        if k <= M :
            s += board[i][k]
        else:
            break
    if s == target or s == target[::-1]:
        cnt += 1
    # 세로
    s = ""
    for k in range(i, i+3):
        if k <= N:
            s += board[k][j]
        else:
            break
    if s == target or s == target[::-1]:
        cnt += 1
    
    # 우측하단 대각선
    s = ""
    for k in range(3):
        if i+k <= N and j+k <= M:
            s += board[i+k][j+k]
        else:
            break
    if s == target or s == target[::-1]:
        cnt += 1

    # 좌측하단 대각선
    s = ""
    for k in range(0, -3, -1):
        if i-k <= N and j+k >= 1:
            s += board[i-k][j+k]
        else:
            break
    if s == target or s == target[::-1]:
        cnt += 1
    return cnt

for _ in range(N):
    l = list(map(str, input()))
    board.append([0] + l)
result = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        result += is_valid(i, j)

print(result)