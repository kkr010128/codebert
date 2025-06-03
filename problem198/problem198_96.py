from collections import *

def dfs(q):
    if len(q)==N:
        print(''.join(q))
        return 
    
    M = 'a'
    
    for qi in q:
        M = max(M, qi)
        
    for i in range(ord(M)-ord('a')+2):
        q.append(alpha[i])
        dfs(q)
        q.pop()

N = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
dfs(deque(['a']))