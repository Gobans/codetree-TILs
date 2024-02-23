N = int(input())
line = list(map(int, input()))

def find_farthest_distance_coordinate():
    farthest_distance = 0
    tempX = 1
    x, y = 0, 1
    cnt = 0
    for i in range(len(line)):
        if i == len(line) - 1:
            if farthest_distance // 2 < cnt:
                x = tempX
                y = i
        elif line[i] == 1 or i == len(line) - 1:
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
    for i in range(len(line)):
        if (line[i] == 1 or i == len(line) - 1) and i != 0:
            if i == len(line) - 1 and line[i] == 0:
                cnt += 1
            nearest_distance = min(nearest_distance, cnt)
            cnt = 0
        else:
            cnt += 1
    return nearest_distance + 1

x, y = find_farthest_distance_coordinate()
if y == len(line) -1:
    line[y] = 1
elif x == 0 and line[0] == 0:
    line[0] = 1
else:
    line[(x+y)//2] = 1
print(find_nearest_distance())