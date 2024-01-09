days = [30, 31, 29]
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
daysMapping = {
    1 : 31,
    2 : 30,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}
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
    if M < 1 or M > 12:
        return -1
    seasonNum = seasonsMapping[M]
    dayNum = daysMapping[M]
    if M == 2 and is_leap_year(Y):
        dayNum = 2
    if D < 1 or D > daysMapping[dayNum]:
        return -1
    print(seasons[seasonNum])

Y, M, D = map(int, input().split())
check_season(Y, M, D)