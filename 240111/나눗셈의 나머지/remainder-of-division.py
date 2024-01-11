a, b = map(int, input().split())
dict = {}
while a > 1:
    remain = a%b
    a = a//b
    if remain in dict:
        dict[remain] += 1
    else:
        dict[remain] = 1
sum = 0
for i in dict.values():
    sum += i*i
print(sum)