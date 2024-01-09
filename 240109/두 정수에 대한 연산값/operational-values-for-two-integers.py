a, b = map(int, input().split())
def processing(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        b += 25
        a *= 2
    return a, b
a, b = processing(a, b)
print(a, b)