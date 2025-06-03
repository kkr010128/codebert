import math
import collections
N,M=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
cumax=(2*10**5)+10
cuml=[0]*cumax
#print(A)
ind=0
l=[]
c=collections.Counter(A)
values=list(c.values())	#aのCollectionのvalue値のリスト(n_1こ、n_2こ…)
key=list(c.keys())	#先のvalue値に相当する要素のリスト(要素1,要素2,…)
for i in range(len(key)):
    l.append([key[i],values[i]])#lは[要素i,n_i]の情報を詰めたmatrix
lr=[]
v=[]
for i in range(len(key)):
    lr.append([0,l[i][0]])
    v.append(l[i][1])
for i in range(len(v)):
    l=lr[i][0]
    r=lr[i][1]
    cuml[l]=cuml[l]+v[i]
    if r+1<cumax:
        cuml[r+1]=cuml[r+1]-v[i]
for i in range(cumax-1):
    cuml[i+1]=cuml[i+1]+cuml[i]
#print(cuml)
maxind=2*10**5+10
minind=0
while maxind-minind>1:
    piv=minind+(maxind-minind)//2       #pivは握手の幸福度
    cnt=0
    for i in range(N):
        x=piv-A[i]
        cnt=cnt+cuml[max(x,0)]
    if cnt<=M:
        maxind=piv
    else:
        minind=piv
    #print(cnt,maxind,piv,minind)
#print(minind)
thr=minind
cuml2=[0]*(N+1)
A.sort(reverse=True)
for i in range(N):
    cuml2[i+1]=cuml2[i]+A[i]
#print(cuml2,thr,A)
ans=0
counts=0
#print(cuml[0:10])
for i in range(N):
    x=thr-A[i]
    #print(x)
    cnt=cuml[max(x,0)]
    #print(cnt)
    ans=ans+(A[i]*cnt)+cuml2[cnt]
    counts=counts+cnt
ans=ans-(counts-M)*thr
#print()
print(ans)