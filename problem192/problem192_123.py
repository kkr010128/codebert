N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
C = {i:0 for i in range(1,N+1)}
for i in range(1,N+1):
    C[A[i]] += 1
tot = 0
for i in range(1,N+1):
    tot += (C[i]*(C[i]-1))//2
for i in range(1,N+1):
    c = C[A[i]]-1
    ans = tot-(C[A[i]]*(C[A[i]]-1))//2+(c*(c-1))//2
    print(ans)