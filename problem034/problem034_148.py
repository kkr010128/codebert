class Dice:
    def __init__(self,u,w,r,s,t,y):
        self.s1 = u
        self.s2= w
        self.s3= r
        self.s4= s
        self.s5 = t
        self.s6= y
    def right_s3(self):
        prev_s3 = self.s3
        self.s3 = prev_s3
    def right_s4(self):
        prev_s4 = self.s4
        self.s3 = prev_s4
    def right_s5(self):
        prev_s5 = self.s5
        self.s3 = prev_s5
    def right_s6(self):
        prev_s6 = self.s6
        self.s3 = prev_s6
    def right_s1(self):
        prev_s1 = self.s1
        self.s3 = prev_s1
    def right_s2(self):
        prev_s2 = self.s2
        self.s3 = prev_s2
    def top(self):
        return self.s3
s1,s2,s3,s4,s5,s6 = map(int,input().split())
order = int(input())
for c in range(order):
    dice = Dice(s1,s2,s3,s4,s5,s6)
    new_s1 , new_s2 = map(int,input().split())
    if (new_s1 == s1 and new_s2 == s2) or (new_s1 ==s2 and new_s2 == s6) or (new_s1 == s6 and new_s2 ==s5) or (new_s1==s5 and new_s2 == s1):
        dice.right_s3()
    elif (new_s1 == s1 and new_s2 == s5) or (new_s1 ==s5 and new_s2 == s6) or (new_s1 == s6 and new_s2 ==s2) or (new_s1==s2 and new_s2 == s1):
        dice.right_s4()
    elif (new_s1 == s1 and new_s2 == s3) or (new_s1 ==s3 and new_s2 == s6) or (new_s1 == s6 and new_s2 ==s4) or (new_s1==s4 and new_s2 == s1):
        dice.right_s5()
    elif (new_s1 == s2 and new_s2 == s4) or (new_s1 ==s4 and new_s2 == s5) or (new_s1 == s5 and new_s2 ==s3) or (new_s1==s3 and new_s2 == s2):
        dice.right_s6()
    elif (new_s1 == s2 and new_s2 == s3) or (new_s1 ==s3 and new_s2 == s5) or (new_s1 == s5 and new_s2 ==s4) or (new_s1==s4 and new_s2 == s2):
        dice.right_s1()
    elif (new_s1 == s1 and new_s2 == s4) or (new_s1 ==s4 and new_s2 == s6) or (new_s1 == s6 and new_s2 ==s3) or (new_s1==s3 and new_s2 == s1):
        dice.right_s2()
    print(dice.top())
