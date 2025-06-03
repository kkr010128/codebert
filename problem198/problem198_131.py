N = int(input())
alpha = [chr(ord("a") + i) for i in range(26)]


def dfs(n, s):
    if len(s) == n:
        print(s)
        return
    cnt = len(set(s))
    cnt += 1

    for a in alpha[:cnt]:
        ns = s + a
        dfs(n, ns)


dfs(N, "")
