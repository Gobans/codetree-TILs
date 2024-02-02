n = int(input())

dist = 0
time = 0
speed = 0

def is_Possible(speed):
    remainDistance = n - dist
    dist_sum = 0
    test_speed = speed
    for _ in range(remainDistance):
        dist_sum += test_speed
        if test_speed > 1:
            test_speed -= 1
    if dist_sum - remainDistance <= 1:
        return True
    return False

slow_down = False
while dist < n:
    if not slow_down and is_Possible(speed + 1):
        speed += 1
    elif is_Possible(speed):
        slow_down = True
    else:
        slow_down = True
        speed -= 1
    dist += speed
    time += 1
print(time)