from datetime import datetime

def find_rainiest_day(data):
    rainy_days = [entry for entry in data if entry[2] == "Rain"]
    rainy_days.sort(key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
    return rainy_days[0]
n = int(input())
data = [input().split() for _ in range(n)]

nearest_rainy_day = find_rainiest_day(data)

print(" ".join(nearest_rainy_day))