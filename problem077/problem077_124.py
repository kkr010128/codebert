a,b,c,d=map(int,input().split())

an=a*c
an=max(an,a*d)
an=max(an,b*c)
an=max(an,b*d)
print(an)