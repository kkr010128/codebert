import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']

ans = []
def dfs(idx, cnt, lis):
    if idx==N:
        ans.append(''.join(lis))
        return
    for i in range(cnt):
        dfs(idx+1, cnt, lis+[alpha[i]])
    dfs(idx+1, cnt+1, lis+[alpha[cnt]])
    return

dfs(0, 0, [])
ans.sort()
for a in ans:
    print(a)