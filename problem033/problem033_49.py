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


faces = list(map(int, input().split()))
cmd = input()

d = Dice()
for c in cmd:
    d.rot(c)

print(faces[d.top()-1])