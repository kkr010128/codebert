import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15

Lunlun = []
K = int(input())

def dfs(i,before):
    if i == 10:
        return
    Lunlun.append(before)
    x = before%10
    for d in (-1,0,1):
        y = x + d
        if y < 0 or y >= 10:
            continue
        dfs(i + 1,before*10 + y)

for i in range(1,10):
    dfs(0,i)
Lunlun.sort()
ans = Lunlun[K - 1]
print(ans)