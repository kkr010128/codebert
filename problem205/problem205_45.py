def main():
    N, P = (int(i) for i in input().split())
    L = [int(s) for s in input()][::-1]
    ans = 0
    if P == 2 or P == 5:
        for i, e in enumerate(L):
            if e % P == 0:
                ans += N-i
    else:
        A = [0]*N
        d = 1
        for i, e in enumerate(L):
            A[i] = (e*d) % P
            d *= 10
            d %= P
        S = [0]*(N+1)
        for i in range(N):
            S[i+1] = S[i] + A[i]
            S[i+1] %= P
        from collections import Counter
        c = Counter(S)
        for v in c.values():
            ans += v*(v-1)//2
    print(ans)


if __name__ == '__main__':
    main()
