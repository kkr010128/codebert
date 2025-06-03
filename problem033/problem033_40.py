class Saikoro:

    def sai(self,one,two,three,four,five,six):
        self.s1=int(one)
        self.s2=int(two)
        self.s3=int(three)
        self.s4=int(four)
        self.s5=int(five)
        self.s6=int(six)

    def turnE(self):
        e=[self.s4,self.s2,self.s1,self.s6,self.s5,self.s3]
        self.s1=e[0]
        self.s2=e[1]
        self.s3=e[2]
        self.s4=e[3]
        self.s5=e[4]
        self.s6=e[5]

    def turnN(self):
        n=[self.s2,self.s6,self.s3,self.s4,self.s1,self.s5]
        self.s1=n[0]
        self.s2=n[1]
        self.s3=n[2]
        self.s4=n[3]
        self.s5=n[4]
        self.s6=n[5]

    def turnS(self):
        s=[self.s5,self.s1,self.s3,self.s4,self.s6,self.s2]
        self.s1=s[0]
        self.s2=s[1]
        self.s3=s[2]
        self.s4=s[3]
        self.s5=s[4]
        self.s6=s[5]

    def turnW(self):
        w=[self.s3,self.s2,self.s6,self.s1,self.s5,self.s4]
        self.s1=w[0]
        self.s2=w[1]
        self.s3=w[2]
        self.s4=w[3]
        self.s5=w[4]
        self.s6=w[5]




l=input().split()
m=list(input())

sai1=Saikoro()
sai1.sai(l[0],l[1],l[2],l[3],l[4],l[5])

n=len(m)
i=0

while i<n:
    if m[i]=="E":
        sai1.turnE()
    elif m[i]=="N":
        sai1.turnN()
    elif m[i]=="S":
        sai1.turnS()
    else:
        sai1.turnW()
    i+=1
print(sai1.s1)
