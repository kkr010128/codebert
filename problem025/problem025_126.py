n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))
"""def dfs(i,m):
    global a
    if i == 0:
        if m == 0:
            return True
        else:
            return False
    if dfs(i-1, m):
        return True
    if dfs(i-1,m - a[i-1]): 
        return True
    return False
for i in range(q):
    if dfs(n,m[i]):
        print("yes")
    else:
        print("no")"""
b = []
def dfs(i,m):
    global b
    if i == 0:
        b.append(m)
    else:
        dfs(i-1,m)
        dfs(i-1,m+a[i-1])
    return b
b = dfs(n,0)
for i in range(q):
    if m[i] in b:
        print("yes")
    else:
        print("no")
