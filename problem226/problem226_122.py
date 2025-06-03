import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

h, n = inm()
a = sorted(inl(), reverse=True)
for i in a:
    h -= i
    if h <= 0:
        break
print("Yes" if h <= 0 else "No")