from functools import reduce
def is_magic_number(n):
    strN = str(n)
    sum = reduce(lambda x, y: int(x) + int(y), strN)
    if n%2 == 0 and sum%5 == 0:
        return "Yes"
    return "No"
n = int(input())
print(is_magic_number(n))