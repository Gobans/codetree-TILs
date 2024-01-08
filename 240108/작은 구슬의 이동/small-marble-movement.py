import sys
n, t = map(int, sys.stdin.readline().split())
r, c, d = sys.stdin.readline().split()
r = int(r)
c = int(c)
mapper = {
    'U' : 0,
    'D' : 3,
    'R' : 1,
    'L' : 2
}
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
dir = mapper[d]
def in_range(x, y):
    return x >= 1 and x <= n and y >= 1 and y <= n
nowt = 0
while nowt <= t:
    r += dys[dir]
    c += dxs[dir]
    if in_range(r, c) == False:
        dir = 3 - dir
        r += dys[dir]
        c += dxs[dir]
        nowt += 1
    nowt += 1
print(r, c)