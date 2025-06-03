import sys
INF = 1 << 60
MOD = 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

def resolve():
    ward = 96
    n, s = map(int, input().split())
    mask = int(('1' * 32 + '0' * 64) * (s + 1) , 2)
    Mask = (1 << (s + 1) * ward) - 1
    dp = 1
    for a in map(int, input().split()):
        dp = (dp * 2) + (dp << ward * a)
        dp &= Mask
        dp = (dp & (~mask)) + ((dp & mask) >> 64) * ((1 << 64) % MOD)

    print(((dp >> s * ward) & ((1 << ward) - 1)) % MOD)
resolve()