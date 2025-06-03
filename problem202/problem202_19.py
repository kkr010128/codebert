n, a, b = map(int,input().split())
ans = 0

if a >= n:
    ans = n
elif a+b >= n:
    ans = a
else:
    set_ab = n//(a+b)
    ans += set_ab*a
    n -= set_ab*(a+b)
    if n < a:
        ans += n
    else:
        ans += a

print(ans)
