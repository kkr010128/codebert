"""
Nが奇数のとき、絶対に末尾が0が来ることはない。したがって、答えは0。
Nが偶数の時、
N//10 * 1 + N//10**2 * 1 + ...の数だけ0ができる。
"""
N = int(input())
if N % 2 == 1:
    print(0)
else:
    ans = 0
    ind = 1
    while True:
        m = 5**ind
        if m > N:
            break
        r = N//m
        r //= 2
        ans += r
        ind += 1
    print(ans)