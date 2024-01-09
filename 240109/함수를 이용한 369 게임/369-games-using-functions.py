def is_magic_number(n):
    strN = str(n)
    if '3' in strN or '6' in strN or '9' in strN:
        return True
    elif n%3 == 0:
        return True
    return False
def count_num(a, b):
    cnt = 0
    for i in range(a,b+1):
        if is_magic_number(i):
            cnt += 1
    print(cnt)
a, b = map(int, input().split())
count_num(a, b)