n,a,b = map(int,input().split())

mod = n%(a+b)
if mod > a :
    ans = a
else:
    ans = mod
ans += (n//(a+b))*a
print(ans)



