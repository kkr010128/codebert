def Judgement(x,y,z):
    if z-x-y>0 and (z-x-y)**2-4*x*y>0:
        return 0
    else:
        return 1

a,b,c=map(int,input().split())
ans=Judgement(a,b,c)
if ans==0:
    print("Yes")
else:
    print("No")