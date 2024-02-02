N = int(input())
pigeons = [ -1 for _ in range(11)]
cnt = 0
for _ in range(N):
    p_idx, road = map(int, input().split())
    if pigeons[p_idx] != -1 and pigeons[p_idx] != road:
        pigeons[p_idx] = road
        cnt += 1
    else:
        pigeons[p_idx] = road
print(cnt)