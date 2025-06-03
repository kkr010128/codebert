def solve():
    N = int(input())
    dfs("", 0, N)

def dfs(cur, n_type, N):
    if len(cur) == N:
        print(cur)
        return
    
    for offset in range(n_type+1):
        next_chr = chr(ord('a') + offset)
        next_n_type = n_type + 1 if offset==n_type else n_type
        dfs(cur+next_chr, next_n_type, N)
    
    return
if __name__ == '__main__':
    solve()