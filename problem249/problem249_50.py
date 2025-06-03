A,B,K=map(int,input().split())

if K<A:
    ans1=A-K
    ans2=B
else:
    ans1=0
    ans2=max(A+B-K,0)

print(ans1,ans2)