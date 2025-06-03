A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
x=[input().split() for l in range(M)]
tot_1=min(a)+min(b)
lis=[]
for i in range(M):
    tot=a[int(x[i][0])-1]+b[int(x[i][1])-1]-int(x[i][2])
    lis.append(tot)
if tot_1<=min(lis):
    print(tot_1)
else:
    print(min(lis))