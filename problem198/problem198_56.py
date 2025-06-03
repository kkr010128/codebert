n = int(input())

ans = []
def dfs(A):
    if len(A) == n:
        ans.append(''.join(A))
        return
    for i in range(len(set(A))+1):
        v = chr(i+ord('a'))
        A.append(v)
        dfs(A)
        A.pop()

dfs([])
ans.sort()
for i in range(len(ans)):
    print(ans[i])
