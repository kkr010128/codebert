class Dice:
    def __init__(self, data):
        self.data = data

    def move(self, direction):
        if direction == 'E':
            self.data[0],self.data[3], self.data[5], self.data[2] = \
                self.data[3],self.data[5], self.data[2], self.data[0] 
        elif direction == 'N':
            self.data[0],self.data[1], self.data[5], self.data[4] = \
                self.data[1],self.data[5], self.data[4], self.data[0]
        elif direction == 'S':
            self.data[0],self.data[1], self.data[5], self.data[4] = \
                self.data[4],self.data[0], self.data[1], self.data[5]
        elif direction == 'W':
            self.data[0],self.data[2], self.data[5], self.data[3] = \
                self.data[2],self.data[5], self.data[3], self.data[0]
        elif direction == 'R':
            self.data[1],self.data[2], self.data[4], self.data[3] = \
                self.data[2],self.data[4], self.data[3], self.data[1]


    def getTop(self):
        return self.data[0]

    def getRight(self, top, front):
        if self.data[0] != top:
            for i in range(4):
                if self.data[0] == top:
                    break
                self.move('E')
            for i in range(4):
                if self.data[0] == top:
                    break
                self.move('N')

        if self.data[1] != front:
            for i in range(3):
                self.move('R')
                if self.data[1] == front and self.data[0] == top:
                    break
        return self.data[2]

dice = Dice(input().split())
hoge = int(input())
fuga = []
for i in range(hoge):
    (x,y) = [j for j in input().split()]
    fuga += [dice.getRight(x,y)]
for i in fuga:
    print(i)