n = int(input())

def dfs(s, mx_idx):
    if len(s) == n:
        print(s)
    else:
        for i in range(mx_idx+1):
            nc = chr(ord('a') + i)
            if i == mx_idx:
                dfs(s + nc, mx_idx + 1)
            else:
                dfs(s+nc, mx_idx)

dfs('a', 1)
