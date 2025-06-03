n,k = map(int, input().split())

ans=n % k

if abs(ans-k)<ans:
    print(abs(ans-k))
else:
    print(ans)
