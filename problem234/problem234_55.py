import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = [[0]*10 for _ in range(10)]

for i in range(1, N+1):
    s = str(i)
    first = int(s[0])
    end = int(s[-1])
    As[first][end] += 1

ans = 0
for i in range(10):
    for j in range(10):
        a = As[i][j]
        b = As[j][i]
        ans += a*b

print(ans)