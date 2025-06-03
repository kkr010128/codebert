import sys
import math
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

n = ini()
a = inl()
x = sum(a) // n
ans = 0
for i in a:
    ans += (i - x) * (i - x)
x = math.ceil(sum(a) / n)
ans2 = 0
for i in a:
    ans2 += (i - x) * (i - x)
print(min(ans, ans2))