n = int(input())
m=list(map(int,input().split()))
A=[0]*n
for i in range(n-1):
    A[m[i]-1]+=1
print(*A, sep = "\n") 
