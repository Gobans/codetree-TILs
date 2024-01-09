def is_complete_number(n):
    if n%2 == 0:
        return False
    if n%10 == 5:
        return False
    if n%3 == 0 and n%9 != 0:
        return False
    return True
def find_answer(a, b):
    cnt = 0
    for i in range(a, b+1):
        if is_complete_number(i):
            cnt += 1
    return cnt

a, b = map(int, input().split()) 
print(find_answer(a, b))