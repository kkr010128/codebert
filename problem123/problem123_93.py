import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())

ALL = 0
for a in As:
    ALL ^= a
ans = [ALL^a for a in As]
print(*ans)