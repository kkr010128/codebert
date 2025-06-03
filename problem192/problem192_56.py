from collections import Counter
N=int(input())
A=list(map(int, input().split()))
C=Counter(A)
# print(C)
ans=0
for k in C:
    n=C.get(k)
    ans+=n*(n-1)//2
# print(ans)

for i in range(N):
    k=A[i]
    n=C.get(k)
    print(ans-n+1)