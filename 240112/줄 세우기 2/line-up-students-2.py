N = int(input())
students = []
class Student:
    def __init__(self, h, w, n):
        self.h = h
        self.w = w
        self.n = n
    def print(self):
        print(self.h, self.w, self.n)
for i in range(1, N+1):
    h, w = map(int, input().split())
    s = Student(h, w, i)
    students.append(s)
students.sort(key = lambda x: (x.h, -x.w))
for i in range(N):
    students[i].print()