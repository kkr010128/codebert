import collections
N = int(input())
A = sorted(list(map(int,input().split())))
cA = collections.Counter(A)

li = [1]*(max(A)+1)
for j in range(N):
    for i in range(A[j]*2,A[-1]+1,A[j]):
        li[i] = 0

for key,val in cA.items():
    if val >1:
        li[key]=0
        
sA = sum([li[i] for i in A])
print(sA)