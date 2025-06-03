N=int(input())
d=list(map(int, input().split()))
sum=0
for i in range(0,N-1):
    for j in range(i+1,N):
        sum=sum+d[i]*d[j]
print(sum)
