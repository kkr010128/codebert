a,b,c,d=map(int,input().split())
prd=[a*c,a*d,b*c,b*d]

if (a<0<b or c<0<d) and max(prd)<0:
    print(0)
else:
    print(max(prd))