def print_star(n, direction, limit):
    print("* "*n)
    if direction == 0 and n > 1:
        n -= 1
        print_star(n, direction, limit)
    elif direction == 1 and n < limit:
        n += 1
        print_star(n, direction, limit)

n = int(input())
print_star(n, 0, n)
print_star(1, 1, n)