import sys
n=int(input())
x=list(map(int,input().split()))

if n==1:
    print('0')
    sys.exit()

if x.count(x[0])==n:
    print('0')
    sys.exit()

a=sum(x)/len(x)
d=[]
for i in range(min(x),max(x)):
    c=0
    for j in x:
        c+=(i-j)**2
    d.append(c)

print(min(d))
