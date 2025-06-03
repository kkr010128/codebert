N=int(input())
A=list(map(int,input().split()))
B=sum(A)
b=0
ans=202020202020
for a in A:
    b+=a
    ans=min(ans,abs(B-b*2))
print(ans)