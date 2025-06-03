def dfs(s, ub, n):
    if len(s) == n:
        print(s)
    else:
        ch = "a"
        while ord(ch) < ord(ub):
            dfs(s + ch, ub, n)
            ch = chr(ord(ch) + 1)
        ub = chr(ord(ub) + 1)
        dfs(s + ch, ub, n)

def solve(n):
    dfs("", "a", n)

n = int(input())
solve(n)