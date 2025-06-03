l = "abcdefghij"


def dfs(a, mx):
    if len(a) == n:
        print(a)
        return
    for i, s in enumerate(l):
        if i == mx+1:
            dfs(a+s, mx+1)
            break
        else:
            dfs(a+s, mx)


n = int(input())
dfs("a", 0)
