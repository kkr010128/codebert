import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
ans = 0
for i, a in enumerate(As, 1):
    if i%2==1 and a%2==1:
        ans += 1
print(ans)