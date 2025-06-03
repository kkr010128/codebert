import math
def solve():

    N = int(input())
    A = list(map(int, input().split()))

    if(N == 0 and A[0] == 1):
        print(1)
        return
    
    leaf_list = [0] * (N+1)
    

    for d in range(N, -1 , -1):
        if(d == N):
            leaf_list[d] = (A[d],A[d])
        else:
            Min = math.ceil(leaf_list[d+1][0]/2) + A[d]
            Max = leaf_list[d+1][1] + A[d]
            leaf_list[d] = (Min,Max)
            
    if(not(leaf_list[0][0] <= 1 and leaf_list[0][1] >= 1)):
        print(-1)
        return
            
    node_list = [0] * (N+1)
    node_list[0] = 1
    
    for d in range(1, N+1):
        node_list[d] = min((node_list[d-1] - A[d-1]) * 2, leaf_list[d][1])
        
    print(sum(node_list))
solve()