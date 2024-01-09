def is_magic_number(n):
    strN = str(n)
    for digit in ['3', '6', '9']:
        if digit in strN:
            return True
    if n%3 == 0:
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