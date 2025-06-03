class dice:
    men = [0] * 7
    def __init__(self, li):
        self.men = [0] + li
    def move(self, h):
        if h == "N":
            t = self.men[1]
            self.men[1] = self.men[2]
            self.men[2] = self.men[6]
            self.men[6] = self.men[5]
            self.men[5] = t
        elif h == "S":
            t = self.men[1]
            self.men[1] = self.men[5]
            self.men[5] = self.men[6]
            self.men[6] = self.men[2]
            self.men[2] = t
        elif h == "W":
            t = self.men[1]
            self.men[1] = self.men[3]
            self.men[3] = self.men[6]
            self.men[6] = self.men[4]
            self.men[4] = t
        elif h == "E":
            t = self.men[1]
            self.men[1] = self.men[4]
            self.men[4] = self.men[6]
            self.men[6] = self.men[3]
            self.men[3] = t
saikoro = dice(list(map(int, input().split())))
for s in input():
    saikoro.move(s)
print(saikoro.men[1])

