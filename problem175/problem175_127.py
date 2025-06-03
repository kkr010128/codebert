import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
S = list(input())
from collections import Counter

c = Counter(S)
ans = c['R']*c['G']*c['B']

for i in range(1, N):
    for j in range(N):
        first, second, third = j, j+i, j+i*2
        if third>=N:
            break
        if len(set((S[first], S[second], S[third])))==3:
            ans -= 1

print(ans)