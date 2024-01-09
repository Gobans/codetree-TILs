def is_leap_year(y):
    if y%4 == 0:
        if y%100 == 0:
            if y%400 == 0:
                return True
            return False
        return True
    return False

y = int(input())
if is_leap_year(y):
    print("true")
else:
    print("false")