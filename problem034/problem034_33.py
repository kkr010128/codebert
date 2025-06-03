class Dice:
    def __init__(self,top,front,right,left,back,bottom):
        self.top, self.bottom=top,bottom
        self.right, self.left=right,left
        self.front, self.back=front,back
    def turn(self,order):
        if order=="N":
            self.top,self.front,self.bottom,self.back=self.front,self.bottom,self.back,self.top
        if order=="S":
            self.top,self.front,self.bottom,self.back=self.back,self.top,self.front,self.bottom
        if order=="E":
            self.top,self.right,self.bottom,self.left=self.left,self.top,self.right,self.bottom
        if order=="W":
            self.top,self.right,self.bottom,self.left=self.right,self.bottom,self.left,self.top

d=map(int,raw_input().split())
dice=Dice(d[0],d[1],d[2],d[3],d[4],d[5])
q=input()
for i in range(q):
    t,f=map(int,raw_input().split())
    if t==d[0]:
        if f==d[1]:
            print d[2]
        elif f==d[2]:
            print d[4]
        elif f==d[4]:
            print d[3]
        elif f==d[3]:
            print d[1]
    elif t==d[1]:
        if f==d[0]:
            print d[3]
        elif f==d[3]:
            print d[5]
        elif f==d[5]:
            print d[2]
        elif f==d[2]:
            print d[0]
    elif t==d[2]:
        if f==d[0]:
            print d[1]
        elif f==d[1]:
            print d[5]
        elif f==d[5]:
            print d[4]
        elif f==d[4]:
            print d[0]
    elif t==d[3]:
        if f==d[0]:
            print d[4]
        elif f==d[4]:
            print d[5]
        elif f==d[5]:
            print d[1]
        elif f==d[1]:
            print d[0]
    elif t==d[4]:
        if f==d[0]:
            print d[2]
        elif f==d[2]:
            print d[5]
        elif f==d[5]:
            print d[3]
        elif f==d[3]:
            print d[0]
    elif t==d[5]:
        if f==d[1]:
            print d[3]
        elif f==d[3]:
            print d[4]
        elif f==d[4]:
            print d[2]
        elif f==d[2]:
            print d[1]
    else:
        print "no answer"
