n = int(input())
for i in range(1, n+1):
    now = 1
    for j in range(i,n+1):
        print(i, "*", now, "=", i*now, end = ' ')
        if j != n:
            print("/", end = ' ')
        now += 1
    print()