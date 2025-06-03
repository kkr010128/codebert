import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    l, r, d = map(int, input().split())
    print(r // d - (l - 1) // d)
resolve()