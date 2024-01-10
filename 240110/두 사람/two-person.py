p1 = input().split()
p2 = input().split()
p1 = (int(p1[0]), p1[1])
p2 = (int(p2[0]), p2[1])
if (p1[0] >= 19 and p1[1] == "M") or (p2[0] >= 19 and p2[1] == "M"):
    print("1")
else:
    print("0")