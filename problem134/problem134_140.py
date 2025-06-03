N=int(input())
A=[int(i) for i in input().split()]
S=set(A)


ans=1
for i in A:
    ans*=i
    if ans>10**18:
        ans=-1
        break
if 0 in S:
    ans=0


print(ans)
