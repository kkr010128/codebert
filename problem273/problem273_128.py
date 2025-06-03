import bisect
import collections
N,K=map(int,input().split())
A=list(map(int,input().split()))
A.insert(0,0)
cuml=[0]*(N+1)
cuml[0]=A[0]
l=[]
cuml2=[]
l2=[]
buf=[]
ans=0
for i in range(N):
    cuml[i+1]=cuml[i]+A[i+1]
#print(cuml)
for i in range(N+1):
    cuml2.append([(cuml[i]-i)%K,i])
    cuml[i]=(cuml[i]-i)%K
#print(cuml2,cuml)
cuml2.sort(key=lambda x:x[0])
piv=cuml2[0][0]
buf=[]
for i in range(N+1):
    if piv!=cuml2[i][0]:
        l2.append(buf)
        piv=cuml2[i][0]
        buf=[]
    buf.append(cuml2[i][1])
l2.append(buf)
#print(l2)
cnt=0
for i in range(len(l2)):
    for j in range(len(l2[i])):
        num=l2[i][j]
        id=bisect.bisect_left(l2[i], num + K)
        #print(j,id)
        cnt=cnt+(id-j-1)
print(cnt)

