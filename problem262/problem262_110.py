from itertools import product

def solve():
    N = int(input())
    graph = {i: [] for i in range(1, N+1)}
    for i in range(N): 
        A = int(input())
        for _ in range(A):
            x,y = map(int, input().split())
            graph[i+1].append((x,y))
            
    def dfs(nodes):
        searched = [-1] * N
        stack = [i+1 for i,node in enumerate(nodes) if node == 1]
        ret_len = len(stack)
        
        while stack:
            node = stack.pop(0)
            for x,y in graph[node]:
                if nodes[x-1] != y: return -1
                if searched[x-1] == -1:
                    searched[x-1] = y
                    if y == 1: stack.append(x)
                        
        # print(nodes, searched)
        return ret_len
                    
        
    ret = 0
    for nodes in product([0,1], repeat=N):
        ret = max(ret, dfs(nodes))
        
    print(ret)
    
solve()