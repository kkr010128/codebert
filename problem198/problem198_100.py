from collections import deque

def dfs(q):
    if len(q)==N:
        print(''.join(q))
        return
    
    for i in range(min(26, ord(max(q))-ord('a')+2)):
        q.append(alpha[i])
        dfs(q)
        q.pop()
    
N = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
dfs(deque(['a']))