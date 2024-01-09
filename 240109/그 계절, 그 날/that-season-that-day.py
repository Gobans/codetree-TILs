seasons = ["Spring", "Summer", "Fall", "Winter"]
seasonsMapping = {
    3 : 0,
    4 : 0,
    5 : 0,
    6 : 1,
    7 : 1,
    8 : 1,
    9 : 2,
    10 : 2,
    11 : 2,
    12 : 3,
    1 : 3,
    2 : 3
}
def find_mx_date(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

def is_leap_year(Y):
    if Y%4 == 0:
        if Y%100 == 0:
            # 윤년임
            if Y%400 == 0:
                return True
            return False
        return True
    return False

def check_season(Y, M, D):
    mx_date = find_mx_date(M, Y)
    if mx_date is None or D > mx_date:
        print(-1)
    else:
        print(seasons[seasonsMapping.get(M)])

Y, M, D = map(int, input().split())
check_season(Y, M, D)