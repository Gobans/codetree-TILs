a, b = map(int, input().split())
exist = 0
for i in range(a, b):
    if 1920%i == 0 and 2880%i == 0:
        exist = 1
        break
print(exist)