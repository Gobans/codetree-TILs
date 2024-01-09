def print_rect(N):
    nowNum = 1
    for _ in range(N):
        for _ in range(N):
            print(nowNum, end = ' ')
            nowNum = (nowNum + 1) % 10
            if nowNum == 0:
                nowNum = 1
        print()
input = int(input())
print_rect(input)