def main():
    import copy
    from heapq import heappop, heapify, heappush
    import math
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    F = [int(i) for i in input().split()]
    ans = 0
    A.sort(reverse=True)
    F.sort()
    s = []
    for i in range(N):
        s.append([A[i]*F[i], A[i], F[i]])
    s.sort(reverse=True, key=lambda x: x[0])

    def f(S, T):
        cur = 0
        num = 0
        while cur <= K:
            if num == N:
                break
            a, b, c = S[num]
            if a <= T:
                break
            cur += math.ceil((a - T)/c)
            num += 1
        if cur <= K:
            return True
        else:
            return False

    ok, ng = s[0][0], -1
    while abs(ok-ng) > 1:
        mid = (ok+ng)//2
        if f(s, mid) == True:
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    main()