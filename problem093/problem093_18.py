# でつoO(YOU PLAY WITH THE CARDS YOU'RE DEALT..)
import sys
INF = 10**10
def main(N, K, P, C):
    ans = max(C)
    for i in range(N):
        used = [False] * N
        now = 0
        mx = -INF
        cnt = 0
        while True:
            if used[i] or cnt >= K:
                break
            used[i] = True
            i = P[i] - 1
            now += C[i]
            mx = max(mx, now)
            cnt += 1
        tmp = max(mx, now)
        if now > 0:
            cycle, mod = divmod(K, cnt)
            if cycle > 1:
                tmp = max(tmp, now * (cycle - 1) + mx)
            t = now * cycle
            tmp = max(tmp, t)
            for j in range(mod):
                i = P[i] - 1
                t += C[i]
                tmp = max(tmp, t)
        ans = max(ans, tmp)
    print(ans)

if __name__ == '__main__':
    input = sys.stdin.readline
    N, K = map(int, input().split())
    *P, = map(int, input().split())
    *C, = map(int, input().split())
    main(N, K, P, C)
