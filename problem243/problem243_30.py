n=int(input())
l=[list(input().split()) for _ in range(n)]
x=input()
ans=0
for i in range(n):
    s,t=l[i]
    t=int(t)
    ans+=t
    if s==x:
        c=ans
print(ans-c)
