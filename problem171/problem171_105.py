import sys
import time

t = time.time()

n = int(input())
a = list(map(int, input().split(' ')))
b = list(range(n))
b.sort(key=lambda x: -a[x])
# print("b after:", b)
# print(list(map(lambda x:a[x],b)))
# print(time.time()-t)

cache = [[-1 for x in range(n)] for y in range(n)]
# print(cache)


def dfs(left, right):
    if left > right:
        return 0
    if cache[left][right] != -1:
        return cache[left][right]
    which = n-(right-left+1)
    ans1 = dfs(left+1, right)+abs(left-b[which])*a[b[which]]
    ans2 = dfs(left, right-1)+abs(right-b[which])*a[b[which]]
    cache[left][right] = max(ans1, ans2)
    return cache[left][right]


sys.setrecursionlimit(2010)
print(dfs(0, n-1))
