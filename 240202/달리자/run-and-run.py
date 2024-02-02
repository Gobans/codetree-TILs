n = int(input())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))
cost = 0
for i in range(n, 1, -1):
    for j in range(i-1, 0, -1):
        distance = i - j
        diff = B[i] - A[i]
        if diff > 0:
            if A[j] <= diff:
                A[i] += A[j]
                cost += A[j] * distance
                A[j] = 0
            else:
                A[i] += diff
                A[j] -= diff
                cost += diff * distance
        else:
            break
print(cost)