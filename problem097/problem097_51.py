K = int(input())
if K%2==0 or K%5==0:
    print(-1)
else:
    ans = 1
    rest = 7%K
    while rest != 0:
        rest *= 10
        rest += 7
        rest %= K
        ans += 1
    print(ans)