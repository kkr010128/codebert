N = int(input())

a_num = 97

def dfs(s, n, cnt): #s: 現在の文字列, n: 残りの文字数, cnt: 現在の文字列の最大の値
    if n == 0:
        print(s)
        return
    for i in range(cnt+2):
        if i == cnt+1:
            dfs(s+chr(a_num+i), n-1, cnt+1)
        else:
            dfs(s+chr(a_num+i), n-1, cnt)

dfs("a", N-1, 0)