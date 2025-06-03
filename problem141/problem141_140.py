N = int(input())
A = list(map(int, input().split()))

def solve(A):
    ans = 0
    leaves = sum(A)
    prev_node_capacity = 1

    for ai in A:
        if ai > prev_node_capacity:
            return -1
        ans += min(prev_node_capacity, leaves)

        leaves -= ai
        prev_node_capacity -= ai
        prev_node_capacity *= 2

    return ans
  
print(solve(A))