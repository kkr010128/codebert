N=int(input())
A=list(map(int,input().split()))
A.sort()
sum=1
for i in range(N):
    sum=sum*A[i]
    if sum>10**18:
        sum=-1
        break

print(sum)