class dice:
    directions = ['S', 'E', 'N', 'W']
    def __init__(self, strlabels):
        label = strlabels.split()
        self.top = label[0]
        self.side = label[1:5]
        self.side[2], self.side[3] = self.side[3], self.side[2]
        self.down = label[5]
        #print(self.top, self.side, self.down)

    def roll(self, direction):
        tmp = self.top
        self.top = self.side[(self.directions.index(direction)+2)%4]
        self.side[(self.directions.index(direction)+2)%4] = self.down
        self.down = self.side[self.directions.index(direction)]
        self.side[self.directions.index(direction)] = tmp
        #print(self.top, self.side, self.down)

    def pFace(self, initial):
        if initial == 'u':
            print(self.top)
        elif initial == 'd':
            print(self.down)
        else:
            print(self.side[directions.index(direction)])

dice1 = dice(input())
for direction in input():
    dice1.roll(direction)

dice1.pFace('u')