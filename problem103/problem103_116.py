N=int(input())
A=list(map(int,input().split()))
m=1000
for i in range(N-1):
    s=0
    if A[i]<A[i+1]:s=m//A[i]
    m+=(A[i+1]-A[i])*s
print(m)