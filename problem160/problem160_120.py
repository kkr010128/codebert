def main():
    N, M, Q = (int(i) for i in input().split())
    T = [[int(i) for i in input().split()] for j in range(Q)]

    def dfs(A):
        if len(A) == N:
            ret = 0
            for (a, b, c, d) in T:
                if A[b-1] - A[a-1] == c:
                    ret += d
            return ret
        ret = 0
        s = A[-1] if A else 1
        for a in range(s, M+1):
            ret = max(ret, dfs(A + [a]))
        return ret

    print(dfs([]))


if __name__ == '__main__':
    main()
