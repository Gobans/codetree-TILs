m1, d1, m2, d2 = map(int, input().split())
target_day = input()
def days_in_month(month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29

def count_days_between_dates(m1, d1, m2, d2, target_day):
    days_in_month1 = days_in_month(m1)
    days_in_month2 = days_in_month(m2)

    current_month = m1
    current_day = d1
    now_day_index = 0
    target_day_index = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].index(target_day)

    count = 0

    while True:
        if target_day_index == now_day_index:
            count += 1

        current_day += 1
        now_day_index = (now_day_index + 1)%7

        if current_day > days_in_month1:
            current_day = 1
            current_month += 1
        if current_month == m2 and current_day == d2:
            if target_day_index == now_day_index:
                count += 1
                break

        days_in_month1 = days_in_month(current_month)


    return count

result = count_days_between_dates(m1, d1, m2, d2, target_day)
print(result)