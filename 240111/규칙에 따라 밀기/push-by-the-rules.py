s = input()
command = input()
l, r = 0, 0
for c in command:
    if c == 'L':
        s = s[1:] + s[0]
    elif c == 'R':
        s = s[-1] + s[:-1]
print(s)