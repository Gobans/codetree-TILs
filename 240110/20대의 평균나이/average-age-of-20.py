l = []
while True:
    try:
        n = int(input())
        if n >= 30:
            answer = sum(l) / len(l)
            print("{:.2f}".format(round(answer, 2)))
        l.append(n)
    except EOFError:
        break