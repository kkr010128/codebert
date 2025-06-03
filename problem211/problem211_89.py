N, R = list(map(int, input().split()))
if N >= 10:
    print(R)
else:
    ans = 100 * (10 - N) + R
    print(ans)