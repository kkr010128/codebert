n=int(input())
a=list(map(int,input().split()))
ans=[0 for s in range(n)]

for i in range(n-1):
    x = int(a[i])
    ans[x-1] +=1

for j in range(n):
    print(ans[j])