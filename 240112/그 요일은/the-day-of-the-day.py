m1, d1, m2, d2 = map(int, input().split())
remainDays = 0
target_day = input()
def days_in_month(month, year):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29

def count_days_between_dates(m1, d1, m2, d2, target_day):
    days_in_month1 = days_in_month(m1, 2024)
    days_in_month2 = days_in_month(m2, 2024)

    current_month = m1
    current_day = d1
    target_day_index = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].index(target_day)

    count = 0

    while current_month != m2 or current_day != d2:
        if current_day == 1:
            target_day_index = (target_day_index + 1) % 7

        if target_day_index == (current_day - 1) % 7:
            count += 1

        current_day += 1

        if current_day > days_in_month1:
            current_day = 1
            current_month += 1

        days_in_month1 = days_in_month(current_month, 2024)

    return count

result = count_days_between_dates(m1, d1, m2, d2, target_day)
print(result)