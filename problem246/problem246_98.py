import math
import itertools

N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
ls=[]
for i in range(1,N+1):
    ls.append(i)
ls2 = list(itertools.permutations(ls,N))
#print(ls2)
cnt1 = 0
cnt2 = 0
for j in range(math.factorial(N)):
    for i in range(N):
        #print(j,i,P[i],ls2[j][i])
        if P[i] == ls2[j][i]:
            cnt1 += 1
        if Q[i] == ls2[j][i]:
            cnt2 += 1
    #print("cnt1",cnt1,"cnt2",cnt2)
    if cnt1 == N:
        a = j
    if cnt2 == N:
        b = j
    cnt1 = 0
    cnt2 = 0
#print(a,b)
print(abs(a-b))
