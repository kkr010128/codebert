class Dice():
    def __init__(self,ary):
        self.top = ary[0]
        self.south = ary[1]
        self.east = ary[2]
        self.west = ary[3]
        self.north = ary[4]
        self.bottom = ary[5]

    def get_top(self):
        return self.top

    def rotate_north(self):
        self.top,self.south,self.north,self.bottom = self.south,self.bottom,self.top,self.north
    
    def rotate_south(self):
        self.top,self.south,self.north,self.bottom = self.north,self.top,self.bottom,self.south

    def rotate_west(self):
        self.top,self.west,self.bottom,self.east = self.east,self.top,self.west,self.bottom

    def rotate_east(self):
        self.top,self.west,self.bottom,self.east = self.west,self.bottom,self.east,self.top

dice = Dice(list(map(int,input().split())))
for i in input():
    if i == "N":
        dice.rotate_north()
    elif i == "E":
        dice.rotate_east()
    elif i == "W":
        dice.rotate_west()
    elif i == "S":
        dice.rotate_south()

top=dice.get_top()
print(top)