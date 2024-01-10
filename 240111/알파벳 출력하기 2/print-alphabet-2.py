n = int(input())
alphabets = list(map(str, "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
idx = 0
for i in range(n):
    for k in range(i):
        print(" ", end = ' ')
    for j in range(i, n):
        print(alphabets[idx], end = ' ')
        if alphabets[idx] == "Z":
            idx = 0
        else:
            idx += 1
    print()