import sys
from itertools import combinations

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W, K = map(int, readline().split())
    S = [readline().strip() for _ in range(H)]

    ans = INF

    for r in range(H):
        for comb in combinations(range(1, H), r):
            sep = [0]
            sep.extend(list(comb))
            sep.append(H)

            res = r
            A = [0] * (r + 1)

            for j in range(W):
                B = [0] * (r + 1)
                for k in range(r + 1):
                    for i in range(sep[k], sep[k + 1]):
                        if S[i][j] == '1':
                            B[k] += 1

                ok = True
                divided = False
                for k in range(r + 1):
                    if B[k] > K:
                        ok = False
                        break
                    if A[k] + B[k] > K:
                        divided = True
                        break
                    else:
                        A[k] += B[k]

                if not ok:
                    res = INF
                    break
                if divided:
                    A = B
                    res += 1

            if ans > res:
                ans = res

    print(ans)
    return


if __name__ == '__main__':
    main()
