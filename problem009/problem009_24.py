from collections import deque

def bfs(maze, visited, x):
    queue = deque([x])
    visited[x] = 1
    ans_list[x] = 0
    while queue:
      #queueには訪れた地点が入っている。そこから、移動できるか考え、queueから消す。
        y = queue.popleft()#queueに入っていたものを消す。
        r = maze[y - 1][2:]
        for i in r:
            if visited[i] == 0:
              if ans_list[i] >= 10 ** 10:
                ans_list[i] = ans_list[y] + 1
                queue.append(i)
    return 0
              

                
if __name__ == "__main__":
  N = int(input())
  A = [0] * N
  for i in range(N):
    A[i] = list(map(int, input().split()))
  visited = [0] * (N + 1)
  ans_list = [float("inf")] * (N + 1)
  bfs(A, visited, 1)
  #print(bfs(A, visited, 1))
  for i in range(1, N + 1):
    if ans_list[i] >= 10 ** 10:
      print(i, -1)
    else:
      print(i, ans_list[i])
                
  
  
  
  
  
  
