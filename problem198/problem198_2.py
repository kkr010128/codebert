from collections import *

def dfs(l):
    if len(l)==N:
        print(''.join(l))
        return
    
    for a in range(ord('a'), ord(max(l))+2):
        l.append(chr(a))
        dfs(l)
        l.pop()
    
N = int(input())
dfs(deque(['a']))