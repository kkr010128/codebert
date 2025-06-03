class Dice:
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.s1 = s1
        self.s2= s2
        self.s3= s3
        self.s4= s4
        self.s5 = s5
        self.s6= s6
    def east(self):
        prev_s1 = self.s1           #prev_s1を固定していないと以前の値が後述でs1に値を代入するとき変わってしまう。
        prev_s3 = self.s3
        prev_s4 = self.s4
        prev_s6 = self.s6
        self.s1 = prev_s4
        self.s3 = prev_s1
        self.s4 = prev_s6
        self.s6 = prev_s3
    def west(self):
        prev_s1 = self.s1
        prev_s3 = self.s3
        prev_s4 = self.s4
        prev_s6 = self.s6
        self.s1 = prev_s3
        self.s3 = prev_s6
        self.s4 = prev_s1
        self.s6 = prev_s4
    def south(self):
        prev_s1 = self.s1
        prev_s2 = self.s2
        prev_s5 = self.s5
        prev_s6 = self.s6
        self.s1 = prev_s5
        self.s2 = prev_s1
        self.s5 = prev_s6
        self.s6 = prev_s2
    def north(self):
        prev_s1 = self.s1
        prev_s2 = self.s2
        prev_s5 = self.s5
        prev_s6 = self.s6
        self.s1 = prev_s2
        self.s2 = prev_s6
        self.s5 = prev_s1
        self.s6 = prev_s5
    def top(self):
        return self.s1
s1,s2,s3,s4,s5,s6 = map(int,input().split())
dice = Dice(s1,s2,s3,s4,s5,s6)
order = input()
for c in order:
    if c =='N':
        dice.north()
    elif c =='S':
        dice.south()
    elif c =='E':
        dice.east()
    elif c == 'W':
        dice.west()
print(dice.top())
