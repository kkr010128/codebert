import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    k = int(input())
    queue = list(range(1, 10))
    cnt = 0
    for v in queue:
        cnt += 1
        if k == cnt:
            print(v)
            return
        r = v % 10
        for d in range(r - 1, r + 2):
            if 0 <= d <= 9:
                queue.append(v * 10 + d)
resolve()