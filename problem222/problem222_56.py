n=int(input())
a=list(map(int,input().split()))
ans=set()
for i in range(n):
    ans.add(a[i])
if len(a)==len(ans):
    print("YES")
else:
    print("NO")