N=int(input())
A=list(map(int,input().split(' ')))
acc = A[0]
S = sum(A)
ans= abs(S-2*acc)
for i in A[1:]:
    acc += i
    ans = min(ans,abs(S-2*acc))
print(ans)