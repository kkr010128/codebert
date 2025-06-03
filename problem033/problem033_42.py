
class Dice:
    def __init__(self,a,b,c,d,e,f):
        self.face1 = a
        self.face2 = b
        self.face3 = c
        self.face4 = d
        self.face5 = e
        self.face6 = f

    def above_face(self):
        return self.face1

    def roll(self, order):
        if order == 'N':
            tmp = self.face1
            self.face1 = self.face2
            self.face2 = self.face6
            self.face6 = self.face5
            self.face5 = tmp
        elif order == 'S':
            tmp = self.face1
            self.face1 = self.face5
            self.face5 = self.face6
            self.face6 = self.face2
            self.face2 = tmp
        elif order == 'W':
            tmp = self.face1
            self.face1 = self.face3
            self.face3 = self.face6
            self.face6 = self.face4
            self.face4 = tmp
        else:
            tmp = self.face1
            self.face1 = self.face4
            self.face4 = self.face6
            self.face6 = self.face3
            self.face3 = tmp

a,b,c,d,e,f = map(int,input().split())
dice1 = Dice(a,b,c,d,e,f)

l_order = list(input())
for i in range(len(l_order)):
    dice1.roll(l_order[i])

print(dice1.above_face())
