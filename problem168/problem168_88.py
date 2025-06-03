n,m = map(int,input().split())
a = [int(i) for i in input().split()]
ans = n - sum(a)
if ans < 0:
    ans = -1
print(ans)