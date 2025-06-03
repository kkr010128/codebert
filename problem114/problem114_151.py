D=int(input())
c=list(map(int,input().split()))
s=[list(map(int,input().split())) for i in range(D)]


test=[int(input()) for i in range(D)]
lastday=[0 for j in range(26)]
points=[0 for i in range(D)]

lastday=[lastday[i]+1 for i in range(26)]
lastday[test[0]-1]=0
minus=sum([x*y for (x,y) in zip(c,lastday)])
points[0]=s[0][test[0]-1]-minus


for i in range(1,D):
    lastday=[lastday[i]+1 for i in range(26)]
    lastday[test[i]-1]=0
    minus=sum([x*y for (x,y) in zip(c,lastday)])
    points[i]=points[i-1]+s[i][test[i]-1]-minus


for ps in points:
    print(ps)