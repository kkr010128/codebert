N=int(input())
A=list(map(int,input().split()))
n=[0 for x in range(N)]
for i in range(N-1):
    n[A[i]-1]+=1
for j in range(N):
    print(n[j])