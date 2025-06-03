N, K = map(int, input().split())
A = list(map(int, input().split()))

A = [-1] + A

loop_pos = None
loop_start_time = None
loop_end_time = None
visited = [-1]*(N+1)
pos = 1
i = 0
while visited[pos] == -1:
    visited[pos] = i
    pos = A[pos]
    i += 1  
    if visited[pos] != -1:
        loop_pos = pos
        loop_start_time = visited[pos]
        loop_end_time = i

# print(loop_start_time, loop_end_time)
w = loop_end_time - loop_start_time
K = min(K, loop_start_time) + max(0, K-loop_start_time)%w
# print(f"K: {K}")

pos = 1
for i in range(K):
    # print(pos)
    pos = A[pos]
print(pos)