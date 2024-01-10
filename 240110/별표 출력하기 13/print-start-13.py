n = int(input())
# for i in range(n):
print("* "*n)
if n >= 2:
    print("* ")
for j in range(n-1, 1, -1):
    print("* "*j)
for j in range(2, n):
    print("* "*j)
if n >= 2:
    print("* ")
print("* "*n)