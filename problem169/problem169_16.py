n=int(input())
a=list(map(int,input().split()))
ans=[0]*(n+1)
for i in a:
    ans[i]+=1
for i in range(n):
    print(ans[i+1])

