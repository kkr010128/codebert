N = int(input())

def dfs(s, mx):
    if len(s) == N:
        print(s)
    else:
        c = 'a'
        while ord(c) <= ord(mx):
            if c == mx:
                dfs(s + c, chr(ord(mx) + 1))
            else:
                dfs(s + c, mx)
            c = chr(ord(c) + 1)

dfs('', 'a')