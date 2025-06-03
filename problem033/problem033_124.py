class Dice:
    def __init__(self, men):
        self.men = men

    def throw(self, direction):
        if direction == "E":
            pmen = men[:]
            men[0] = pmen[3]
            men[1] = pmen[1]
            men[2] = pmen[0]
            men[3] = pmen[5]
            men[4] = pmen[4]
            men[5] = pmen[2]
        elif direction == "W":
            pmen = men[:]
            men[0] = pmen[2]
            men[1] = pmen[1]
            men[2] = pmen[5]
            men[3] = pmen[0]
            men[4] = pmen[4]
            men[5] = pmen[3]
        elif direction == "S":
            pmen = men[:]
            men[0] = pmen[4]
            men[1] = pmen[0]
            men[2] = pmen[2]
            men[3] = pmen[3]
            men[4] = pmen[5]
            men[5] = pmen[1]
        elif direction == "N":
            pmen = men[:]
            men[0] = pmen[1]
            men[1] = pmen[5]
            men[2] = pmen[2]
            men[3] = pmen[3]
            men[4] = pmen[0]
            men[5] = pmen[4]


    def printUe(self):
        print (self.men)[0]

    def printMen(self):
        print self.men

men = map(int, (raw_input()).split(" "))
d = Dice(men)

S = raw_input()
for s in S:
    d.throw(s)
d.printUe()