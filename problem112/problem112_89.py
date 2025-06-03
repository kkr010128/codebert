def e_multiplication_4(MOD=10**9 + 7):
    from functools import reduce
    N, K = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]

    sign = {-1: 0, 0: 0, 1: 0}  # A の各要素の符号
    for a in A:
        if a == 0:
            sign[0] += 1
            continue
        sign[a // abs(a)] += 1

    if sign[1] == 0 and K % 2 == 1:
        # どうやっても解は負。絶対値の小さなものから掛けていく
        A.sort(reverse=True)
        return reduce(lambda x, y: (x * y) % MOD, A[:K])
    if sign[1] == 0 and K % 2 == 0:
        # 先程と違って絶対値の大きなものから掛けても解は正になる
        A.sort()
        return reduce(lambda x, y: (x * y) % MOD, A[:K])

    A.sort()
    ans = 1
    i, j = 0, N - 1
    while K > 0:
        # 負の絶対値が大きいものから 2 個取るか？　正の絶対値が大きいものから 1 個取るか？
        # i, j がそれぞれ負の値、非負の値を指さなくなった場合、if 文のどちらかを
        # 確実に通らなくなるので、i, j についての条件は必要ない
        if K > 1 and A[i] * A[i + 1] >= A[j] * A[j - 1]:
            ans *= A[i] * A[i + 1]
            i += 2
            K -= 2
        else:
            ans *= A[j]
            j -= 1
            K -= 1
        ans %= MOD
    return ans

print(e_multiplication_4())