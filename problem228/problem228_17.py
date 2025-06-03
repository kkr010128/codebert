import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

n = ini()
ans = 0
tmp = 1
while n > 0:
    n //= 2
    ans += tmp
    tmp *= 2
print(ans)