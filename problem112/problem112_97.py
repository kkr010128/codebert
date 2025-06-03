N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7


def solve(N, K, A):
    ans = 1
    # K = N の場合は明らか
    if K == N:
        for i in range(K):
            ans *= A[i]
            ans %= MOD
    # Ai の全ての数が負かつ K が奇数のとき、
    elif max(A) < 0 and K % 2 == 1:
        A.sort(reverse=True)
        # 絶対値が小さい方から K 個の積
        for i in range(K):
            ans *= A[i]
            ans %= MOD
    # それ以外の場合、積は必ず非負
    else:
        # {Ai} を絶対値の降順にソート
        A.sort(key=abs, reverse=True)
        # 最初の K 個の積
        sign = 1
        for i in range(K):
            ans *= A[i]
            ans %= MOD
            if A[i] < 0:
                sign *= -1
            elif A[i] == 0:
                sign *= 0
        # P が負の場合
        if sign < 0:
            small_nonneg = [a for a in A[K:] if a >= 0]
            small_neg = [a for a in A[K:] if a < 0]
            large_nonneg = [a for a in A[:K] if a >= 0]
            large_neg = [a for a in A[:K] if a < 0]
            if not small_neg or not large_nonneg:
                ans *= max(small_nonneg)
                ans %= MOD
                ans *= pow(max(large_neg), MOD - 2, MOD)
                ans %= MOD
            elif not small_nonneg or not large_neg:
                ans *= min(small_neg)
                ans %= MOD
                ans *= pow(min(large_nonneg), MOD - 2, MOD)
                ans %= MOD
            else:
                if min(small_neg) * max(large_neg) > max(small_nonneg) * min(
                    large_nonneg
                ):
                    # (2) 正の数を 1 つ取り除き、負の数を 1 つ加える
                    ans *= min(small_neg)
                    ans %= MOD
                    ans *= pow(min(large_nonneg), MOD - 2, MOD)
                    ans %= MOD
                else:
                    # (1) 負の数を 1 つ取り除き、非負の数を 1 つ加える
                    ans *= max(small_nonneg)
                    ans %= MOD
                    ans *= pow(max(large_neg), MOD - 2, MOD)
                    ans %= MOD
    return ans


print(solve(N, K, A))
