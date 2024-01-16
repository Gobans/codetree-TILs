a = list(map(int, input()))
changed = False
for i in range(len(a)):
    if a[i] == 0:
        changed = True
        a[i] = 1
        break
if not changed:
    for i in range(len(a)-1, 0, -1):
        if a[i] == 1:
            changed = True
            a[i] = 0
            break
num = 0
for i in a:
    num = num * 2 + i
print(num)