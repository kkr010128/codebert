def dfs(S, mx):
    if len(S) == N:
        print(S)
    else:
        for i in range(a, mx+2):
            if i == mx+1:
                dfs(S+chr(i), mx+1)
            else:
                dfs(S+chr(i), mx)
    return

N = int(input())
a = ord('a')
dfs('a', a)