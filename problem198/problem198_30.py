n = int(input())

d = 'abcdefghijklm'


def conv(s):
    s = list(map(lambda x: d[x], s))
    return ''.join(s)


def dfs(s, k):
    if len(s) == n:
        print(s)
    else:
        for i in range(k):
            dfs(s+d[i], k)
        dfs(s+d[k], k+1)


dfs('a', 1)
