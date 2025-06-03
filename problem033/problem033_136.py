# import dice
class dice:
    def __init__(self):
        self.top = 1
        # self.srf = [[2,4,3,5],[6,4,3,1],[6,2,5,1],[6,5,2,1],[6,4,3,1],[5,4,3,2]]
        self.bottom = 2
        self.up = 5
        self.left = 4
        self.right = 3
        self.reverse = 6
    def move(self, dim):
        if dim == "N":
            temp = self.top
            self.top = self.bottom
            self.bottom = self.reverse
            self.reverse = self.up
            self.up = temp
        elif dim == "E":
            temp = self.top
            self.top = self.left
            self.left = self.reverse
            self.reverse = self.right
            self.right = temp
        elif dim == "W":
            temp = self.top
            self.top = self.right
            self.right = self.reverse
            self.reverse = self.left
            self.left = temp
        elif dim == "S":
            temp = self.top
            self.top = self.up
            self.up = self.reverse
            self.reverse = self.bottom
            self.bottom = temp

x = []
x = list(map(int, input().split()))
mv = []
mv = list(input())
dc = dice()

for i in range(len(mv)):
    dc.move(mv[i])
    
print(x[dc.top - 1])
    
