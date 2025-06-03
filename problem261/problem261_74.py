import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())
leng = len(S)
ans = 0
for i in range(leng//2):
    if S[i]!=S[-i-1]:
        ans += 1
print(ans)