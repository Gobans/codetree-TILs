n = int(input())
num = 9
for _ in range(n):
    for _ in range(n):
        print(num, end = '')
        num = num - 1
        if num == 0:
            num = 9
    print()