S = int(input())

kMod = 10**9+7

memo = {}

def count(n):
    if n < 3:
        return 0
    if n in memo:
        return memo[n]
    ans = 1
    for i in range(3, n+1):
        ans += count(n-i)
        ans %= kMod
    memo[n] = ans
    return ans

print(count(S))