class Dice:
    def __init__(self, labels):
        self.up = labels[0]
        self.front = labels[1]
        self.right = labels[2]
        self.left = labels[3]
        self.back = labels[4]
        self.down = labels[5]
    def east(self):
        self.up, self.right, self.down, self.left = self.left, self.up, self.right, self.down
    def north(self):
        self.up, self.back, self.down, self.front = self.front, self.up, self.back, self.down
    def south(self):
        self.up, self.front, self.down, self.back = self.back, self.up, self.front, self.down
    def west(self):
        self.up, self.left, self.down, self.right = self.right, self.up, self.left, self.down

dice = Dice(list(map(int, input().split())))
for cmd in list(input()):
    if cmd == 'E':
        dice.east()
    if cmd == 'N':
        dice.north()
    if cmd == 'S':
        dice.south()
    if cmd == 'W':
        dice.west()
print(dice.up)