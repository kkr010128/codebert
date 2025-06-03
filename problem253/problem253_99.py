n, a, b = map(int, input().split())
if (b-a)%2 == 0:
    ans = (b-a)//2
else:
    ans = 0
    if a-1 <= n-b:
        ans += a
        a, b = 1, b-a
        ans += (b-a)//2
    else:
        ans += n-b+1
        a, b = a+n-b+1, n
        ans += (b-a)//2
print(ans)
