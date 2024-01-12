n = int(input())
l = list(map(int, input().split()))
ar = []
for i in range(n):
    ar.append(l[i])
    if (i+1)%2 == 1:
        ar.sort()
        print(ar[len(ar)//2], end = ' ')