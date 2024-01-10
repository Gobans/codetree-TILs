n = int(input())
e, o = 1, 0
inputs = []
for i in range(1, n+1):
    if i%2 == 1:
        print("* "*(n-o))
        inputs.append("* "*(n-o))
        o += 1
    else:
        print("* "*e)
        inputs.append("* "*e)
        e += 1
for _ in range(1, n+1):
    print(inputs.pop())