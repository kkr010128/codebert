class Dice:
    def __init__(self, data):
        self.data = data

    def move(self, direction):
        if direction == 'E':
            self.data[0],self.data[3],self.data[5],self.data[2] = \
                    self.data[3],self.data[5],self.data[2],self.data[0]
        elif direction == 'N':
            self.data[0],self.data[4],self.data[5],self.data[1] = \
                    self.data[1],self.data[0],self.data[4],self.data[5]
        elif direction == 'S':
            self.data[0],self.data[1],self.data[5],self.data[4] = \
                    self.data[4],self.data[0],self.data[1],self.data[5]
        elif direction == 'W':
             self.data[0],self.data[2],self.data[5],self.data[3] = \
                    self.data[2],self.data[5],self.data[3],self.data[0]
        elif direction == 'LEFT':
            self.data[2],self.data[4],self.data[3],self.data[1] = \
                    self.data[1], self.data[2],self.data[4],self.data[3]


    def getTop(self):
        return self.data[0]

    def getRight(self):
        return self.data[2]

    def moveTopTo(self, target):
        for i in range(4):
            if self.data[0] == target:
                break
            self.move('W')

            if self.data[1] == target:
                self.move('S')
            elif self.data[4] == target:
                self.move('N')

    def moveFrontTo(self, target):
        for i in range(4):
            if self.data[1] == target:
                break
            self.move('LEFT')

dice = Dice(input().split())
count = int(input())
result = []

for i in range(count):
    (top, front) = [i for i in input().split()]
    dice.moveTopTo(top)
    dice.moveFrontTo(front)
    result.append(dice.getRight())

for s in result:
    print(s)