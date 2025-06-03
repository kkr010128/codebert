import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
Hs = list(mapint())

lis = [1 if a>=K else 0 for a in Hs]
print(sum(lis))