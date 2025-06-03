class Dice :
    def __init__(self,num):
        self.num = num

    def move_E(self):
        self.copy = self.num.copy() 
        for i,j in zip([0,2,5,3],[3,0,2,5]):
            self.num[i] = self.copy[j]

    def move_W(self):
        self.copy = self.num.copy()
        for i,j in zip([0,3,5,2],[2,0,3,5]):
            self.num[i] = self.copy[j]

    def move_N(self):
        self.copy = self.num.copy()
        for i,j in zip([0,1,5,4],[1,5,4,0]):
            self.num[i] = self.copy[j]

    def move_S(self):
        self.copy = self.num.copy()
        for i,j in zip([0,1,5,4],[4,0,1,5]):
            self.num[i] = self.copy[j]



number = list(map(int,input().split()))
#number = [1,2,4,8,16,32]
#print("1 2 3 4 5 6")
# ?????????????????????
dice = Dice(number)

for order in input():
    if order == 'S':
        dice.move_S()
    elif order == 'N':
        dice.move_N()
    elif order == 'W':
        dice.move_W()
    else:
        dice.move_E()

# ?????????????????¶????????????
#print(dice.num)

print(dice.num[0])