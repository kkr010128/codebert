from bisect import bisect_left
import numpy


def main():
    def isOK(score):
        count = 0
        for a in reversed(A):
            border_score = score - a
            index = bleft(A, border_score)
            count += N - index
            if count >= M:
                return True
        return False

    N, M = map(int, input().split())
    A = sorted(map(int, input().split()))
    ans = 0

    ng = A[-1] + A[-1] + 1
    ok = A[0] + A[0]
    bleft = bisect_left

    while(abs(ok-ng) > 1):
        #print(ok, ng)
        mid = (ok+ng) // 2
        f = isOK(mid)
        if f:
            ok = mid
        else:
            ng = mid
        #print(f)
        #print(ok, ng)
    C = [0,] + A
    C = numpy.cumsum(C[::-1])
    #print(C)
    min_score = float('inf')
    count = 0
    for a in reversed(A):
        index = bleft(A, ok-a)
        if index < N:
            min_score = min(a+A[index], min_score)
            ans += C[N-index-1] + (N-index) * a
            count += N-index

    ans -= min_score * (count-M)
    print(ans)


if __name__ == '__main__':
    main()
