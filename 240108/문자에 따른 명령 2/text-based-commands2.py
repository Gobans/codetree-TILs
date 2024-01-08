import sys
input = sys.stdin.readline()
input = str(input)
x, y = 0, 0
nowDir = 0
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for command in input:
    if command == "L":
        nowDir = (nowDir - 1 + 4) % 4
    elif command == "R":
        nowDir = (nowDir + 1) % 4
    elif command == "F":
        mx, my = dir[nowDir]
        x += mx
        y += my
print(x, y)