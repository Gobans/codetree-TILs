def days_in_month(month):
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    elif month in {4, 6, 9, 11}:
        return 30
    elif month == 2:
        return 29

def count_days_between_dates(m1, d1, m2, d2, target_day):
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    target_index = days_of_week.index(target_day)
    
    current_index = 0
    count = 0
    now_days_in_month = days_in_month(m1)
    
    while True:
        current_index = (current_index + 1) % 7

        if current_index == target_index:
            count += 1

        if m1 == m2 and d1 == d2:
            break
        d1 += 1
        if d1 > now_days_in_month:
            d1 = 1
            m1 += 1
            now_days_in_month = days_in_month(m1)

    return count

m1, d1, m2, d2 = map(int, input().split())
target_day = input().strip()

result = count_days_between_dates(m1, d1, m2, d2, target_day)
print(result)