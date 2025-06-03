import sys

n=int(input())
A=list(map(int,input().split()))
p=10**9+7

status=[1,0,0]
ans=3

if A[0]!=0:
    print(0)
    sys.exit()

for i in range(1,n):
    count=status.count(A[i])
    if count==0:
        print(0)
        sys.exit()
    
    ans=(ans*count)%p
    status[status.index(A[i])]+=1

print(ans)