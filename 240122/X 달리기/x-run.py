import sys
x = int(input())
min_time = sys.maxsize

def running(distance, speed, time):
    global min_time
    if distance > x or min_time <= time:
        return
    if distance == x and speed == 1:
        min_time = min(min_time, time)
        return
    elif distance = x and speed > 1:
        return
    
    now_distance = distance + speed
    running(now_distance, speed, time + 1)
    running(now_distance, speed + 1, time + 1)
    if speed > 1:
        running(now_distance, speed -1, time + 1)

running(0, 1, 1)
print(min_time)