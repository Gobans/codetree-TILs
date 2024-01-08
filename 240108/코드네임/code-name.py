class Agent:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print(self):
        print(self.name + " " + str(self.score))

agents = []
for _ in range(5):
    name, score = input().split()
    score = int(score)
    agents.append(Agent(name, score))

agents.sort(key = lambda x: x.score)
agents[0].print()