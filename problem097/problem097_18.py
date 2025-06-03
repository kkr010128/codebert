k = int(input())
if k%2==0 or k%5==0:
    print(-1)
else:
    ans = 1
    res = 7
    while True:
        if res%k == 0:
            print(ans)
            break
        res = res*10+7
        res %= k
        ans += 1