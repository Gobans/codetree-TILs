class Agent:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time
    def talk(self):
        print("secret code : " + self.code)
        print("meeting point : " + self.place)
        print("time : " + self.time)
code, place, time = input().split()

a = Agent(code, place, time)
a.talk()