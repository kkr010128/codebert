import sys
input = sys.stdin.buffer.readline
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n, k = MAP()
h = LIST()
h.sort(reverse=True)

if k >= n:
    print(0)
else:
    print(sum(h[k:]))
