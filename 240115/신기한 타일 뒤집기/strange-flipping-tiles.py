n = int(input())
now_position = 0
positions = {}

for _ in range(n):
    x, c = input().split()
    x = int(x)
    if c == "L":
        now = str(now_position)
        positions[now] = True
        for _ in range(x-1):
            now_position -= 1
            now = str(now_position)
            positions[now] = True
    else:
        now = str(now_position)
        positions[now] = False
        for _ in range(x-1):
            now_position += 1
            now = str(now_position)
            positions[now] = False
black = 0
white = 0

for value in positions.values():
    if value == True:
        white += 1
    else:
        black += 1
print(white, black)