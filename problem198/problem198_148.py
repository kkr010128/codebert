n = int(input())


def dfs(n, s, idx):
    l = len(s)
    if n == l:
        print(s)
        return
    alpha = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while i < idx + 1:
        if i == idx:
            dfs(n, s + alpha[i], idx + 1)
        else:
            dfs(n, s + alpha[i], idx)
        i += 1


dfs(n, "", 0)

