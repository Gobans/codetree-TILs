# 가위바위보 셋트를 저장, 각각 가정을 

N = int(input())
dict = {}
for i in range(N):
    a, b = map(int, input().split())
    for i in range(1, 4):
        rock = i
        for j in range(1, 4):
            if j == rock:
                continue
            scissor = j
            for k in range(1, 4):
                if k == scissor or k == rock:
                    continue
                papaer = k
                if (a == rock and b == scissor) or (a == scissor and b == papaer) or (a == papaer and b == rock):
                    key = (rock, scissor, papaer)
                    if key in dict:
                        dict[key] += 1
                    else:
                        dict[key] = 1

print(max(dict.values()))