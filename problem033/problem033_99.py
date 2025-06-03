class Dice(object):
    """docstring for Dice"""
    def __init__(self, numeric_column):
        self.numeric_column=numeric_column
    def roll_to_S_direction(self):
        self.numeric_column=[self.numeric_column[4],self.numeric_column[0],self.numeric_column[2],self.numeric_column[3],self.numeric_column[5],self.numeric_column[1]]
    def roll_to_N_direction(self):
        self.numeric_column=[self.numeric_column[1],self.numeric_column[5],self.numeric_column[2],self.numeric_column[3],self.numeric_column[0],self.numeric_column[4]]
    def roll_to_E_direction(self):
        self.numeric_column=[self.numeric_column[3],self.numeric_column[1],self.numeric_column[0],self.numeric_column[5],self.numeric_column[4],self.numeric_column[2]]
    def roll_to_W_direction(self):
        self.numeric_column=[self.numeric_column[2],self.numeric_column[1],self.numeric_column[5],self.numeric_column[0],self.numeric_column[4],self.numeric_column[3]]

dice=Dice(map(int,raw_input().split()))
direction=raw_input()
for i in direction:
    if i=='S': dice.roll_to_S_direction()
    elif i=='N': dice.roll_to_N_direction()
    elif i=='E': dice.roll_to_E_direction()
    else: dice.roll_to_W_direction()
print dice.numeric_column[0]