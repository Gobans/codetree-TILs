binary = list(map(int,input()))
num = 0

for i in range(5):
    num = num * 2 + binary[i]

print(num)