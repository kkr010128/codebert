a,b=map(int,input().split())
ans=a-b*2
if a<=b*2:
    ans=0
print(ans)