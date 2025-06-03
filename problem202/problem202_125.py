n,a,b = map(int,input().split())
A=n//(a+b)
B=n%(a+b)
ans = a * A
if B>=a:
    ans += a
else:
    ans += B 
print(ans)