from itertools import permutations as per
n=int(input())
ans=[]
l=list(per(list(range(1,n+1))))
xy=[[] for i in range(n+1)]
for i in range(n):
    x,y=map(int,input().split())
    xy[i+1].append(x)
    xy[i+1].append(y)
def f(x):
    m=1
    while x>0:
        m*=x
        x=x-1
    return m
for i in range(f(n)):
    dis=0
    for j in range(n-1):
        dis+=((xy[l[i][j]][0]-xy[l[i][j+1]][0])**2+(xy[l[i][j]][1]-xy[l[i][j+1]][1])**2)**(0.5)
    ans.append(dis)
print(sum(ans)/f(n))
    


