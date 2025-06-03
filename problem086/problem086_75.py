n,x,t=map(int, input().split())
tako = n//x
amari = n%x
ans = tako*t
if amari != 0:
    ans += t
print(ans)