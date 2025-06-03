# coding: utf-8
# Your code here!
import bisect

N,D,A=map(int,input().split())

log=[]
loc=[]
ene=[]

for _ in range(N):
    X,H=map(int,input().split())
    log.append([X,H])

log.sort(key=lambda x:x[0])

for X,H in log:
    loc.append(X)
    ene.append(H)

syokan=[0]*N

power=0
for i in range(N):
    temp=max(-((-ene[i]+power)//A),0)*A
    power+=temp
    
    rng=bisect.bisect_right(loc,loc[i]+2*D)
    syokan[min(rng-1,N-1)]+=temp
    
    power-=syokan[i]
    #print(syokan)
#print(syokan)
print(sum(syokan)//A)