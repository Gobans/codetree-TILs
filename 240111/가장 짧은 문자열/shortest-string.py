a = []
for _ in range(3):
    i = input()
    a.append(len(i))
print(max(a) - min(a))