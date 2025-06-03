# https://atcoder.jp/contests/abc146/submissions/8617148

def solve(N, M, S):
    from collections import namedtuple
    from heapq import heappop, heappush

    INF = N * 2
    V = namedtuple('V', 'cnt index')

    cnt_from_N = [INF] * (N + 1)
    cnt_from_N[N] = 0

    parent = [0] * (N + 1)

    h = [V(cnt=0, index=N)]

    for j in range(N - 1, -1, -1):
        # S[j]に到達する最小回数とその経路を求める
        if S[j]:
            continue

        while h:
            cnt, par = h[0]
            if par > j + M:
                # jまで移動できない(距離>M)
                heappop(h)
                continue
            break
            # jまで最小回数で到達できる頂点par
            # parまでの回数cnt

        if not h:
            return -1,
            # jまで到達できる頂点がない

        cnt_from_N[j] = cnt + 1
        parent[j] = par

        heappush(h, V(cnt=cnt + 1, index=j))

    ret = []
    curr = 0
    while curr < N:
        par = parent[curr]
        ret.append(par - curr)
        curr = par

    return ret


def main():
    N, M = map(int, input().split())
    *S, = map(int, input())
    print(*solve(N, M, S))


if __name__ == '__main__':
    main()
