n = int(input())

L = [0]*n
for i in range(n):
    L[i] = chr(i+ord('a'))
#print(L)_

ans = []
def dfs(A):
    if len(A) == n:
        ans.append(''.join(A))
        return
    for v in L[0:len(set(A))+1]:
        A.append(v)
        dfs(A)
        A.pop()

dfs([])
ans.sort()
for i in range(len(ans)):
    print(ans[i])
