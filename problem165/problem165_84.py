import sys
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

seen = set()
t = ini()
for _ in range(t):
    s = ins()
    seen.add(s)
print(len(seen))