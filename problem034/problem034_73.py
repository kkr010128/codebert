import random

class  Dise:
    def __init__(self,top,flont,right,left,back,bottom):
        self.top,self.flont,self.right,self.left,self.back,self.bottom=top,flont,right,left,back,bottom
        
    def rot(self,d):
        if d=='N':
            self.top,self.flont,self.bottom,self.back=self.flont,self.bottom,self.back,self.top
        elif d=='E':
            self.top,self.right,self.bottom,self.left=self.left,self.top,self.right,self.bottom
        elif d=='S':
                self.top,self.flont,self.bottom,self.back=self.back,self.top,self.flont,self.bottom
        elif d=='W':
            self.top,self.right,self.bottom,self.left=self.right,self.bottom,self.left,self.top
    
    def gettop(self):
        return self.top
    def getfront(self):
        return self.flont
    def getright(self):
        return self.right

n=list(map(int,input().split()))
m=int(input())
dise=Dise(n[0],n[1],n[2],n[3],n[4],n[5])

for i in range(m):
    a,b=(int(x) for x in input().split())
    for j in range(1000):
        dise.rot(random.choice('NESW'))
        if a==dise.gettop() and b==dise.getfront():
            print(dise.getright())
            break

            
        
