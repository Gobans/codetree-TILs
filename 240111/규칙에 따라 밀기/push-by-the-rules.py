s = input()
command = input()
l, r = 0, 0
for c in command:
    if c == "L":
        if r > 0:
            r -= 1
        else:
            l += 1
    else:
        if l > 0:
            l -= 1
        else:
            r += 1
for _ in range(l):
    tmp = s[0]
    s = s[1:]
    s += tmp
for _ in range(r):
    tmp = s[-1]
    s = s[:-2]
    s = tmp + s
print(s)