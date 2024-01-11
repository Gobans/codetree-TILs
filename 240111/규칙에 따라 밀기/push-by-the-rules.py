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
s = s[l:] + s[:-r] if r > 0 else s[l:]

print(s)