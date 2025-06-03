import bisect


def calc_pairs(p, A):
    # （Aは昇順にソート済であることが前提）
    # 和の値がp以上となる組の個数を返す
    pairs = 0
    N = len(A)
    for a in A:
        j = bisect.bisect_left(A, p - a)
        pairs += N - j
    return pairs


def main():
    N, M = list(map(int, input().split(' ')))
    A = list(map(int, input().split(' ')))
    A.sort()
    cumsum_A = [a for a in A]
    for i in range(1, N):
        cumsum_A[i] += cumsum_A[i - 1]
    # 次を満たす最大のpを求める：「和がp以上となる組の数がM以上」
    ok, ng = 0, 2 * A[-1] + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if calc_pairs(mid, A) >= M:
            ok = mid
        else:
            ng = mid
    # 和がp(=ok)以上となる組の値の合計を出す
    ans = 0
    for a in A:
        index = bisect.bisect_left(A, ok - a)
        v = (N - index) * a + cumsum_A[N - 1] - (0 if index == 0 else cumsum_A[index - 1])
        ans += v
    # M組を超えてしまった分を差し引く
    pairs = calc_pairs(ok, A)
    ans -= (pairs - M) * ok
    print(ans)


if __name__ == '__main__':
    main()