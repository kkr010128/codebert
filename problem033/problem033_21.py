class Dice:
    def __init__(self,t,f,r,l,b,u):
        self.t=t
        self.f=f
        self.r=r
        self.l=l
        self.b=b
        self.u=u
    def roll(self,i):
        if d=='S':
            key=self.t
            self.t=self.b
            self.b=self.u
            self.u=self.f
            self.f=key
        elif d=='E':
            key=self.t
            self.t=self.l
            self.l=self.u
            self.u=self.r
            self.r=key
        elif d=='N':
            key=self.t
            self.t=self.f
            self.f=self.u
            self.u=self.b
            self.b=key
        else:
            key=self.t
            self.t=self.r
            self.r=self.u
            self.u=self.l
            self.l=key
t,f,r,l,b,u=map(int,input().split())
a=list(input())
dice=Dice(t,f,r,l,b,u)
for d in a:
    dice.roll(d)
print(dice.t)
