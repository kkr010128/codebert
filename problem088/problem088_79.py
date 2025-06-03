N=int(input())
A=list(map(int,input().split()))
count=0
for i in range(N-1):
    if A[i+1] < A[i]:
        count=count+A[i]-A[i+1]
        A[i+1]=A[i]
    else:
        count=count
print(count)