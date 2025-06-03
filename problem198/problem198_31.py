import sys
input = sys.stdin.readline

n = int(input())

a_ord = ord('a')

s = ["a"]

ans = []

def dfs(s):
    max_ord = a_ord
    for i in s:
        max_ord = max(max_ord, ord(i))
    for i in range(a_ord, max_ord + 2):
        t = s[:]
        t.append(chr(i))
        if len(t) == n:
            ans.append("".join(t))
        else:
            dfs(t)
if n == 1:
    print('a')
else:
    dfs(s)
    ans.sort()
    for w in ans:
        print(w)