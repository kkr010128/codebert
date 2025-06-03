a,b,c,k = list(map(int,input().split()))

ans = 0
if a >= k:
    print(k)
elif a+b >= k:
    print(a)
else:
    ans += a
    k -= (a+b)
    ans -= k
    print(ans)
