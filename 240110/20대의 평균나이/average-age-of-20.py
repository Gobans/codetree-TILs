l = []
while True:
    try:
        n = int(input())
        if not n in range(20, 30):
            answer = round(sum(l) / len(l), 2)
            print("{:.2f}".format(answer))
            break
        l.append(n)
    except EOFError:
        break