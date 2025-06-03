import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))
out = lambda x: print('\n'.join(map(str, x)))

n = ini()
s = list(ins())
n = s.count("R")
t = sorted(s)
ans = 0
for i in range(n):
    if s[i] != t[i]:
        ans += 1
print(ans)