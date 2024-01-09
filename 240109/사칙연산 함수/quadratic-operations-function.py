def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def divide(a, b):
    return int(a / b)
def multiple(a, b):
    return a*b

a, o, c = input().split()
print(a + " " + o + " " + c + " = ", end = '')
a = int(a)
c = int(c)
if o == '+':
    answer = plus(a, c)
elif o == '-':
    answer = minus(a, c)
elif o == '*':
    answer = multiple(a, c)
elif o == '/':
    answer = divide(a, c)
else:
    print("False")
print(answer)