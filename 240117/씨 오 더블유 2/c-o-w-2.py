N = int(input())
s = input()
cnt = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if s[i] == "C" and s[j] == "O" and s[k] == "W":
                cnt += 1
print(cnt)