m1, d1, m2, d2 = map(int, input().split())
remainDays = 0
days = [31,29,31,30,31,30,31,31,30,31,30,31]
dof = input()
for m in range(m1, m2+1):
    r = 0
    if m == m1:
        r = days[m1-1] - d1
    elif m == m2:
        r = d2
    else:
        r = days[m]
    remainDays += r
dofs = ["", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
answer = 0
answer += remainDays//7
if dof in dofs[:remainDays%7+1]:
    answer += 1
print(answer)