N = int(input())
line = list(map(int, input()))

def find_farthest_distance_coordinate():
    farthest_distance = 0
    tempX = 1
    x, y = 1, 1
    cnt = 0
    for i in range(1, len(line)):
        if line[i] == 1:
            farthest_distance = max(farthest_distance, cnt)
            if farthest_distance == cnt:
                x = tempX
                y = i
            tempX = i
            cnt = 0
        else:
            cnt += 1
    return (x, y)

def find_nearest_distance():
    nearest_distance = len(line)
    cnt = 0
    for i in range(1, len(line)):
        if line[i] == 1:
            nearest_distance = min(nearest_distance, cnt)
            cnt = 0
        else:
            cnt += 1
    return nearest_distance + 1

x, y = find_farthest_distance_coordinate()
line[(x+y)//2] = 1
print(find_nearest_distance())