l = []
a1, a2 = map(int, input().split())
l.append(a1)
l.append(a2)
for i in range(2, 10):
    newA = l[i-1] + 2*l[i-2]
    l.append(newA)
print(*l)