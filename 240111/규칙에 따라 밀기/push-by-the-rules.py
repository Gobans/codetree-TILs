s = input()
command = input()
l, r = 0, 0
for c in command:
    if c == "L":
        l += 1
    else:
        r += 1
s = s[l:] + s[:-r] if r > 0 else s[l:]
print(s)