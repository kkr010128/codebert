class Dice:
    TOP, SOUTH, EAST, WEST, NORTH, BOTTOM = 0, 1, 2, 3, 4, 5
    def __init__(self, d):
        self.dice = d
        self.top = d[0]
        self.south = d[1]
        self.east = d[2]
        self.west = d[3]
        self.north = d[4]
        self.bottom = d[5]

    def set_top_front(self, top, front):
        for i, n in enumerate(self.dice):
            if n == top:
                if i == Dice.TOP: pass
                elif i == Dice.SOUTH: self.move("N")
                elif i == Dice.EAST: self.move("W")
                elif i == Dice.WEST: self.move("E")
                elif i == Dice.NORTH: self.move("S")
                elif i == Dice.BOTTOM:
                    self.move("S")
                    self.move("S")

                break
        
        for i, n in enumerate(self.dice):
            if n == front:
                if i == Dice.TOP: print("error.")
                elif i == Dice.SOUTH: pass
                elif i == Dice.EAST: self.move("R")
                elif i == Dice.WEST: self.move("L")
                elif i == Dice.NORTH:
                    self.move("R")
                    self.move("R")
                elif i == Dice.BOTTOM: print("error.")

                break
            
        
    def move(self, d):
        if d == "N":
            self.move_north()
        elif d == "W":
            self.move_west()
        elif d == "S":
            self.move_south()
        elif d == "E":
            self.move_east()
        elif d == "R":
            self.move_right()
        elif d == "L":
            self.move_left()

        self.dice = [
            self.top,
            self.south,
            self.east,
            self.west,
            self.north,
            self.bottom,
        ]

    def move_right(self):
        self.north, self.west, self.south, self.east \
            = self.west, self.south, self.east, self.north

    def move_left(self):
        self.north, self.west, self.south, self.east \
            = self.east, self.north, self.west, self.south

    def move_north(self):
        self.top, self.south, self.bottom, self.north \
            = self.south, self.bottom, self.north, self.top

    def move_south(self):
        self.top, self.south, self.bottom, self.north \
            = self.north, self.top, self.south, self.bottom

    def move_east(self):
        self.top, self.east, self.bottom, self.west \
            = self.west, self.top, self.east, self.bottom

    def move_west(self):
        self.top, self.east, self.bottom, self.west \
            = self.east, self.bottom, self.west, self.top

if __name__ == "__main__":
    import re

    nums = [int(n) for n in re.split(r"\s+", input().strip())]
    dice = Dice(nums)

    n = int(input().strip())
    for i in range(n):
        top, front = [int(n) for n in re.split(r"\s+", input().strip())]
        dice.set_top_front(top, front)

        print(dice.east)

