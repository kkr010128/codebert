from numba import njit

n = int(input())

@njit
def solve():
    f = [1] * (n + 1)
    for i in range(2, n + 1):
        if f[i] != 1: continue
        m = i
        while m <= n:
            tmp = m
            cnt = 0
            while tmp % i == 0:
                tmp = tmp // i
                cnt += 1
            f[m] *= cnt + 1
            m += i
    ans = 0
    for i in range(1, n + 1):
        ans += i * f[i]
    return ans

print(solve())