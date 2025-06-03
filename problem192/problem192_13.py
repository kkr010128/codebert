N=int(input())
A=list(map(int,input().split()))

count=[0 for i in range(N)]
for i in A:
    count[i-1]+=1
    
def chose(n):
    return int(n*(n-1)/2)

total=0
for i in count:
    total+=chose(i)

for i in range(N):
    ans=total
    ans-=chose(count[A[i]-1])
    count[A[i]-1]-=1
    ans+=chose(count[A[i]-1])
    count[A[i]-1]+=1
    print(ans)