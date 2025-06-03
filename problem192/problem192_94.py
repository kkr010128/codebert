N=int(input())
A=list(map(int,input().strip().split()))

l=[0 for n in range(N)]

for e in A:
    l[e-1]+=1

count=0
for n in range(N):
    if l[n]>=2:
        count+=l[n]*(l[n]-1)//2
            
for n in range(N):
    print(count-l[A[n]-1]+1)