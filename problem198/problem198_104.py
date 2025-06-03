n = int(input())

ansl = []
def dfs(s, max_s):
    if len(s) == n:
        ansl.append(s)
        return
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(max_s+1):
        dfs(s+ascii_lowercase[i], max(i+1, max_s))

dfs("", 0)
for a in ansl:
    print(a)