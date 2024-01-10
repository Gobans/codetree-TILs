answer = 1
for _ in range(5):
    n = int(input())
    if n%3 != 0:
        answer = 0
        break
print(answer)