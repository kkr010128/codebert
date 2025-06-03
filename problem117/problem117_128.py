from bisect import bisect_right

def bisectsearch_right(L,a):
    i=bisect_right(L,a)
    return(i)

N,M,K= list(map(int, input().split()))
A= list(map(int, input().split()))
B= list(map(int, input().split()))

Asum=[0]*N
Bsum=[0]*M
Asum[0]=A[0]
Bsum[0]=B[0]
for i in range(1,N):
    Asum[i]=Asum[i-1]+A[i]
for j in range(1,M):
    Bsum[j]=Bsum[j-1]+B[j]
# print(Asum)
# print(Bsum)
ans=[0]*(N+1)
ans[0]=bisectsearch_right(Bsum,K)
# print(ans[0])
for i in range(1,N+1):
    if Asum[i-1]>K:
        continue
    j=bisectsearch_right(Bsum,K-Asum[i-1])
    # print(j)
    ans[i]=i+j
# print(ans)
print(max(ans))
