# dictionary 에 선분 좌표마다 저장.
# 선분 하나를 제거했을떄, 선분의 dictionary 의 값중 1이 존재한다면 겹치고 있는것, 아니면 겹치지 않는것 

n = int(input())
lines = []
my_dict = {}
for _ in range(n):
    x1, x2 = map(int, input().split())
    lines.append((x1, x2))
    for i in range(x1, x2+1):
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

def is_overlapped(x1, x2):
    for i in range(x1, x2+1):
        if my_dict[i] >=2:
            return True
    return False

possible = False
for i in range(n):
    overlapped = True
    x1, x2 = lines[i]
    for j in range(x1, x2+1):
        my_dict[j] -= 1
    for j in range(i+1, n):
        x3, x4 = lines[j]
        if not is_overlapped(x3, x4):
            overlapped = False
            break
        if not overlapped:
            break
    if overlapped:
        possible = True
        break
    for j in range(x1, x2+1):
        if j in my_dict:
            my_dict[j] += 1
        else:
            my_dict[j] = 1
if possible:
    print("Yes")
else:
    print("No")