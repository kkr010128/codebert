class Dice(object):
    def __init__(self, top, south, east, west, north, bottom):
        self.top = top
        self.south = south
        self.east = east
        self.west = west
        self.north = north
        self.bottom = bottom

    def get_top(self):
        return self.top

    def rotate(self, directions):
        for direction in directions:
            if direction == 'S':
                self.prev_top = self.top
                self.top = self.north
                self.north = self.bottom
                self.bottom = self.south
                self.south = self.prev_top
            elif direction == 'E':
                self.prev_top = self.top
                self.top = self.west
                self.west = self.bottom
                self.bottom = self.east
                self.east = self.prev_top
            elif direction == 'W':
                self.prev_top = self.top
                self.top = self.east
                self.east = self.bottom
                self.bottom = self.west
                self.west = self.prev_top
            elif direction == 'N':
                self.prev_top = self.top
                self.top = self.south
                self.south = self.bottom
                self.bottom = self.north
                self.north = self.prev_top

dice = Dice(*map(int, input().split()))
dice.rotate(input())
print(dice.get_top())