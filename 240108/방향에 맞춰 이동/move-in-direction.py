import sys
N = int(sys.stdin.readline())
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
x, y = 0, 0
for i in range(N):
    dr, ds = sys.stdin.readline().split()
    ds = int(ds)
    if dr == "W":
        x += dx[2]*ds
    elif dr == "S":
        y += dy[1]*ds
    elif dr == "N":
        y += dy[0]*ds
    elif dr == "E":
        x += dx[3]*ds
print(x, y)