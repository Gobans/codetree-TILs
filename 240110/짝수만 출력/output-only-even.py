a, b = map(int, input().split())
while a <= b:
    a += 1
    if a %2 == 0:
        print(a, end = ' ')