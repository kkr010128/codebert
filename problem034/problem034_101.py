class Dice(object):
    
    def __init__(self, line):
        self.top = 1
        self.bottom = 6
        self.south = 2
        self.east = 3
        self.west = 4
        self.north = 5
        self.convert = [int(s) for s in line.split()]
    
    def move(self, direction):
        if 'N' == direction:
            self.top, self.north, self.bottom, self.south = self.south, self.top, self.north, self.bottom
        elif 'S' == direction:
            self.top, self.north, self.bottom, self.south = self.north, self.bottom, self.south, self.top
        elif 'W' == direction:
            self.top, self.east, self.bottom, self.west = self.east, self.bottom, self.west, self.top
        elif 'E' == direction:
            self.top, self.east, self.bottom, self.west = self.west, self.top, self.east, self.bottom
    
    def search(self, line):
        top, south = [int(s) for s in line.split()]
        for direction in 'NNNNWNNNN':
            self.move(direction)
            if self.convert[self.south - 1] == south:
                break
        for direction in 'WWWW':
            self.move(direction)
            if self.convert[self.top - 1] == top:
                break
        return self.result()
        
    def result(self):
        return self.convert[self.east - 1]
    
dice = Dice(input())
for i in range(int(input())):
    print(dice.search(input()))