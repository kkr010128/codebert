import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    xor = 0
    for a in A:
        xor ^= a
    ans = [a ^ xor for a in A]
    print(*ans)
resolve()