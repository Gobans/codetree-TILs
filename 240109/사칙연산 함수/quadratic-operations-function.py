def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def divide(a, b):
    return int(a / b)
def multiple(a, b):
    return a*b

def calculate(a, o, c):
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
        return
    print(str(a) + " " + str(o) + " " + str(c) + " = " + str(answer), end = '')


a, o, c = input().split()
a = int(a)
c = int(c)
calculate(a, o, c)