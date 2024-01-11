s1 = input()
s2 = input()
num1 = ""
num2 = ""
numbers = "0123456789"
for c in s1:
    if c in numbers:
        num1 += c
for c in s2:
    if c in numbers:
        num2 += c
print(int(num1) + int(num2))