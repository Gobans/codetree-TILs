N = int(input())
def plus_sum(N):
    sum = 0
    for i in range(1, N+1):
        sum += i
    return int(sum / 10)
print(plus_sum(N))