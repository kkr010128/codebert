class Dice:
    def __init__(self,labels):
       self.stat =  labels
    
    def roll_E(self):
        self.stat[0],self.stat[2],self.stat[3],self.stat[5] = self.stat[3],self.stat[0],self.stat[5],self.stat[2]
        
    def roll_N(self):
        self.stat[0],self.stat[1],self.stat[5],self.stat[4] = self.stat[1],self.stat[5],self.stat[4],self.stat[0]
        
    def roll_S(self):
        self.stat[0],self.stat[1],self.stat[5],self.stat[4] = self.stat[4],self.stat[0],self.stat[1],self.stat[5]
        
    def roll_W(self):
        self.stat[0],self.stat[2],self.stat[5],self.stat[3] = self.stat[2],self.stat[5],self.stat[3],self.stat[0]
        
    def get_top(self):
        return self.stat[0]
        
dice = Dice(input().split())
commands = input()

for command in commands:
    if command == "E":
        dice.roll_E()
    elif command == "N":
        dice.roll_N()
    elif command == "S":
        dice.roll_S()
    elif command == "W":
        dice.roll_W()

print(dice.get_top())
