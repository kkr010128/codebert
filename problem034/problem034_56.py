class Dice:
    def __init__(self,dice):
        self.dice = dice
        
    
    
    def dice_num(self,a,b):
        if (a==2 and b == 4) or (a==3 and b==1) or (a==4 and b==3) or (a==1 and b== 2):
            return self.dice[0]
        elif (a==2 and b == 0) or (a==0 and b==3) or (a==3 and b==5) or (a==5 and b== 2):
            return self.dice[1]
        elif (a==4 and b == 0) or (a==0 and b==1) or (a==5 and b==4) or (a==1 and b== 5):
            return self.dice[2]
        elif (a==0 and b == 4) or (a==4 and b==5) or (a==5 and b==1) or (a==1 and b== 0):
            return self.dice[3]
        elif (a==2 and b == 5) or (a==3 and b==0) or (a==0 and b==2) or (a==5 and b== 3):
            return self.dice[4]
        else:
            return self.dice[5]
            
    
    
dice = list(map(int,input().split()))

n = int(input())
        
for _ in range(n):
    a,b = map(int,input().split())
    a_num = dice.index(a)
    b_num = dice.index(b)
    dice_2 = Dice(dice)
    print(dice_2.dice_num(a_num,b_num))
