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
    def clockwise(self):
        self.front, self.left, self.back, self.right = self.right, self.front, self.left, self.back
    def counterclockwise(self):
        self.front, self.right, self.back, self.left = self.left, self.front, self.right, self.back
    def set_up(self, up):
        for i in range(6):
            if up == self.up:
                break
            if i % 2:
                self.east()
            else:
                self.north()
    def set_front(self, front):
        while True:
            if front == self.front:
                break
            self.clockwise()

dice = Dice(list(map(int, input().split())))
for _ in range(int(input())):
    up, front = map(int, input().split())
    dice.set_up(up)
    dice.set_front(front)
    print(dice.right)