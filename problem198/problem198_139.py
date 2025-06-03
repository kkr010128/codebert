N = int(input())

lis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def dfs(ans, keep, n):
    if n == N + 1:
        print(ans)
    else:
        for i in range(keep):
            dfs(ans + lis[i], max(keep, i + 2), n + 1)


dfs('', 1, 1)
