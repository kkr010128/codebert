import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    now = 0
    for _ in range(n):
        x, y = map(int, input().split())
        if x == y:
            now += 1
        else:
            now = 0
        if now == 3:
            print("Yes")
            return
    print("No")
resolve()