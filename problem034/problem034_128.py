class Dice:
    def __init__(self):
        self.faces=[]

    def rotate(self, direction):
        tmp = self.faces.copy()

        if direction =="N":
            self.faces[5-1] = tmp[1-1]
            self.faces[1-1] = tmp[2-1]
            self.faces[2-1] = tmp[6-1]
            self.faces[6-1] = tmp[5-1]
        if direction =="S":
            self.faces[5-1] = tmp[6-1]
            self.faces[1-1] = tmp[5-1]
            self.faces[2-1] = tmp[1-1]
            self.faces[6-1] = tmp[2-1]
        if direction =="W":
            self.faces[4-1] = tmp[1-1]
            self.faces[1-1] = tmp[3-1]
            self.faces[3-1] = tmp[6-1]
            self.faces[6-1] = tmp[4-1]
        if direction =="E":
            self.faces[3-1] = tmp[1-1]
            self.faces[1-1] = tmp[4-1]
            self.faces[4-1] = tmp[6-1]
            self.faces[6-1] = tmp[3-1]
        return 0

    def spin(self):
        self.faces[4-1], self.faces[2-1],self.faces[5-1],self.faces[3-1] =\
        self.faces[2-1], self.faces[3-1],self.faces[4-1],self.faces[5-1]

        return 0

d1 = Dice()
d1.faces=[int(x) for x in input().split(" ")]
lines = int(input())
for i in range(lines):
    up, front = map(int, input().split(" "))
    #set up side
    for _ in range(3):
        if d1.faces[0] == up:
            break
        d1.rotate("N")

    for _ in range(3):
        if d1.faces[0] == up:
            break
        d1.rotate("W")

    #set front side
    for _ in range(3):
        if d1.faces[1] == front:
            break
        d1.spin()

    print(d1.faces[2])