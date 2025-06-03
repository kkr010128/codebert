n=int(input())
a=list(map(int,input().split()))
s=sum(a)
ans = 12345678901234
cnt = 0
for i in range(n):
    cnt += a[i]
    ans = min(ans,abs(s-cnt - cnt))
print(ans)