from collections import deque

mod = int(1e9+7)
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    n, m = map(int,raw_input().split())
    
    adj_list = [[] for _ in range(n+5)]
    
    q = deque()
    
    ans = [-1] * (n+5)
    
    failed = False
    
    for _ in range(m):
        a, b = map(int,raw_input().split())    
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    q.append(1)
    
    #print(adj_list)
    
    visited = set()
    
    visited.add(1)
    
    while len(q):
        sz = len(q)
        for _ in range(sz):
            cur = q.popleft()
            for nei in adj_list[cur]:
                if nei not in visited:
                    ans[nei] = cur
                    q.append(nei)
                    visited.add(nei)
    
    
    print('Yes')
    for i in range(2, n+1):
        print(ans[i])
            
            
        
        
    
    

main()