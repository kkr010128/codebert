n = int(input())

d = 'abcdefghijklm'


def conv(s):
    s = list(map(lambda x: d[x], s))
    return ''.join(s)


def dfs(s):
    if len(s) == n:
        print(conv(s))
    else:
        mx = max(s)+1
        for i in range(mx+1):
            dfs(s+[i])


dfs([0])