n = int(input())
arr = []
for _ in range(n):
    a = input()
    arr.append(a)
c = input()
cnt = 0
length = 0
for i in range(n):
    if arr[i][0] == c:
       cnt += 1 
       length += len(arr[i])
print(cnt, "{:.2f}".format(round(length // cnt, 2)))