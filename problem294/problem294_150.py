def resolve():
    N = int(input())
    L = sorted(list(map(int, input().split())))
    # print(L)
    ans = 0
    import bisect
    for i in range(N):
        for j in range(i+1, N):
            a, b = L[i], L[j]
            idx1 = bisect.bisect_left(L,b+a)
            idx2 = bisect.bisect_right(L,b-a)
            cnt = idx1 - idx2
            if idx2 <= i <= idx1:
                cnt -= 1
            if idx2 <= j <= idx1:
                cnt -= 1
            if cnt > 0:
                ans += cnt
            # print("a: {} b: {} i: {} j: {} idx1: {}, idx2: {}".format(a, b, i, j, idx1, idx2))
            # print(ans)
    print(ans//3)
    

if '__main__' == __name__:
    resolve()