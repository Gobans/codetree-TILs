class User:
    def __init__(self, id = "codetree", lv = "10"):
        self.id = id
        self.lv = lv
    def print(self):
        print("user " + self.id + " lv " + self.lv)

u = User()
u.print()
id, lv = input().split()
u.id = id
u.lv = lv
u.print()