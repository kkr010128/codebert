N=int(input())
A=list(map(int, input().split()))
ans=[0]*N
for i in range(N-1):
    a=A[i]
    ans[a-1]+=1

for a in ans:
    print(a)