n, m = map(int, input().split())
board1 = []
for _ in range(n):
    line = list(map(int, input().split()))
    board1.append(line)
answerBoard = []
for i in range(n):
    line = list(map(int, input().split()))
    newLine = []
    for j in range(m):
        if board1[i][j] == line[j]:
            newLine.append(0)
        else:
            newLine.append(1)
    answerBoard.append(newLine)
for i in range(n):
    print(*answerBoard[i])