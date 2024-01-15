l = input()
cnt = 0
for i in range(len(l)):
    if l[i] == "(":
        for j in range(i+1, len(l)):
            if l[j] == ")":
                cnt += 1

print(cnt)