import sys
l = list(map(int, input().split()))
min_diff = sys.maxsize 
for i in range(4):
    for j in range(i+1, 5):
        team1 = l[i] + l[j]
        for k in range(4):
            for m in range(i+1, 5):
                if k not in [i, j] and m not in [i, j]:
                    team2 = l[k] + l[m]
                    for n in range(5):
                        if n not in [i, j, k, m]:
                            team3 = l[n]
                            if team1 == team2 or team2 == team3 or team1 == team3:
                                continue
                            max_team = max(team1, team2, team3)
                            min_team = min(team1, team2, team3)
                            min_diff = min(min_diff, max_team - min_team)
print(min_diff)