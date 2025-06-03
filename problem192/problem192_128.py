from collections import Counter
N=int(input())
A = list(map(int,input().split()))
ans = [0] * N
B = Counter(A)
for i in range(N):
    ans[i] = B[A[i]]-1

total=sum(ans)
C=[]
for i in range(N):
    c = (total-2*ans[i])//2
    C.append(c)

for num in C:
    print(num)