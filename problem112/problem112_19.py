from heapq import heappop, heappush

MOD = int(1e9+7)


def div(a, b):
    return a * pow(b, MOD-2, MOD) % MOD


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    q = []
    numneg = 0
    for a in A:
        if a < 0:
            heappush(q, [a, "n"])
            numneg += 1
        elif a >= 0:
            heappush(q, [-a, "p"])
    if K % 2 == 1 and numneg == N or N == K:
        ans = 1
        A.sort(reverse=True)
        for i in range(K):
            ans = (ans * A[i]) % MOD
        print(ans)
        return
    ans = 1
    is_positive = True
    prevpos = None
    prevneg = None
    for i in range(K):
        num, posneg = heappop(q)
        ans = (ans * -num) % MOD
        if posneg == "n":
            is_positive = not is_positive
            prevneg = num
        else:
            prevpos = num
    if ans != 0 and not is_positive:
        nextpos = None
        nextneg = None
        while len(q) and (nextneg is None or nextpos is None):
            num, posneg = heappop(q)
            if posneg == "p" and nextpos is None:
                nextpos = num
            elif posneg == "n" and nextneg is None:
                nextneg = num
        # nextneg / prevpos < nextpos / prevneg
        if prevpos is None or nextneg is None:
            ans = div(ans * nextpos, prevneg)
        elif prevneg is None or nextpos is None:
            ans = div(ans * nextneg, prevpos)
        else:
            if nextneg * prevneg < nextpos * prevpos:
                ans = div(ans * nextpos, prevneg)
            else:
                ans = div(ans * nextneg, prevpos)
    print(ans)


if __name__ == "__main__":
    main()
