def count_days_between_dates(m1, d1, m2, d2, target_day):
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    
    # Find the index of the target day
    target_index = days_of_week.index(target_day)
    
    # Initialize variables
    current_day = (d1 - 1 + sum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m1-1])) % 7
    count = 0
    
    # Loop through days between the two dates
    while m1 != m2 or d1 != d2:
        current_day = (current_day + 1) % 7
        
        # Check if the current day is the target day
        if current_day == target_index:
            count += 1
        
        # Move to the next day
        d1 += 1
        if d1 > 31:
            d1 = 1
            m1 += 1
    
    return count

# Input reading
m1, d1, m2, d2 = map(int, input().split())
target_day = input().strip()

# Output the result
result = count_days_between_dates(m1, d1, m2, d2, target_day)
print(result)