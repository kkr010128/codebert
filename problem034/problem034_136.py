class Dice:
    dice = {'N':2, 'E':4, 'S':5, 'W':3}
    currTop = 1

    def top(self):
        return self.currTop

    def rot(self, direction):
        newTop = self.dice[direction]
        currTop = self.currTop
        self.currTop = newTop
        if direction == 'N':
            self.dice['N'] = 7 - currTop
            self.dice['S'] = currTop
        elif direction == 'S':
            self.dice['N'] = currTop
            self.dice['S'] = 7 - currTop
        elif direction == 'E':
            self.dice['E'] = 7 - currTop
            self.dice['W'] = currTop
        elif direction == 'W':
            self.dice['E'] = currTop
            self.dice['W'] = 7 - currTop

    def yaw(self, direction):
        newDice = {}
        if direction == 'E':
            newDice['N'] = self.dice['E']
            newDice['E'] = self.dice['S']
            newDice['S'] = self.dice['W']
            newDice['W'] = self.dice['N']
        if direction == 'W':
            newDice['N'] = self.dice['W']
            newDice['E'] = self.dice['N']
            newDice['S'] = self.dice['E']
            newDice['W'] = self.dice['S']
        self.dice = newDice

faces = list(map(int, input().split()))
q = int(input())
d = Dice()

for i in range(q):
    top, front = list(map(int, input().split()))
    topIdx = faces.index(top) + 1
    frontIdx = faces.index(front) + 1

    if d.top() != topIdx:
        # search topIdx and rotate to make topIdx top.
        key = [k for k,v in d.dice.items() if topIdx == v]
        if len(key) == 0:
            d.rot('N')
            key = [k for k,v in d.dice.items() if topIdx == v]
        d.rot(key[0])

    # rotate(yaw) to make frontIdx front.
    while True:
        if d.dice['N'] == frontIdx:
            break
        d.yaw('E')

    print(faces[d.dice['W']-1])