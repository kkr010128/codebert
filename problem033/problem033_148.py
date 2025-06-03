class Dice:
    def __init__(self,numbers):
        self.surface=numbers

    def roll_E(self):
        self.surface[0],self.surface[2],self.surface[3],self.surface[5]=self.surface[3],self.surface[0],self.surface[5],self.surface[2]
    def roll_N(self):
        self.surface[0],self.surface[1],self.surface[4],self.surface[5]=self.surface[1],self.surface[5],self.surface[0],self.surface[4]
    def roll_S(self):
        self.surface[0],self.surface[1],self.surface[4],self.surface[5]=self.surface[4],self.surface[0],self.surface[5],self.surface[1]
    def roll_W(self):
        self.surface[0],self.surface[2],self.surface[3],self.surface[5]=self.surface[2],self.surface[5],self.surface[0],self.surface[3]
    def result(self):
        return self.surface[0]

dice=Dice(input().split())
orders=input()
for i in orders:
    if i=='E':
        dice.roll_E()
    if i=='N':
        dice.roll_N()
    if i=='S':
        dice.roll_S()
    if i=='W':
        dice.roll_W()
print(int(dice.result()))
