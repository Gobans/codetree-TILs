n = int(input())
for i in range(0, n):
    if i == 0:
        print("* "*n)
    else:
        print("* "*i + "  "*(n-i-1) + "*")