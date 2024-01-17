A = input()
a_len = len(A)
cnt = 0
for i in range(a_len-3):
    for j in range(i+2, a_len-1):
        if A[i] == "(" and A[i+1] == "(" and A[j] == ")" and A[j+1] == ")":
            cnt += 1
print(cnt)