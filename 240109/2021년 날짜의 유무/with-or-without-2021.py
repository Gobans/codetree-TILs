def is_exist(M, D):
    if M > 12:
        print("No")
        return
    if M in [1, 3, 5, 7, 8, 10, 12]:
        day = 31
    elif M is 2:
        day = 28
    else:
        day = 30
    if D > day:
        print("No")
        return
    print("Yes")
M, D = map(int, input().split())
is_exist(M, D)