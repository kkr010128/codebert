from itertools import accumulate
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
ruiseki = list(accumulate(A[::-1]))

def syakutori(mid):
    x = 0
    cnt = 0
    ans = 0
    for i in range(N)[::-1]: # 大きい方から
        while x < N:
            if A[i] + A[x] >= mid:
                cnt += N - x
                if N - x >= 1:
                    ans += A[i] * (N - x) + ruiseki[N - x - 1]
                break
            else:
                x += 1

    return cnt, ans

# 自分以上の数の個数がM個以上になる値のうち最大のもの
ok = 0
ng = 10 ** 15
while ok + 1 < ng:
    mid = (ok + ng) // 2
    cnt, ans = syakutori(mid)
    if cnt >= M:
        ok = mid
    else:
        ng = mid
# okで終わってる場合はcntがM個以上の場合があるから過分を引く
# ngで終わってる場合は残りM-cnt個のokを足す
print(ans + ok * (M - cnt)) 