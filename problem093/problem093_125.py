N, K = map(int, input().split())
moves = [0] + list(map(int, input().split()))
points = [0] + list(map(int, input().split()))
INF = 10**10
 
answer = -INF
for start in range(1, N+1):
  circle = [start]
  next = moves[start]
  c_score = points[start]
  while(next != start):
    circle.append(next)
    c_score += points[next]
    next = moves[next]
  m_score = 0
  for i in range(min(len(circle), K)):
    m_score += points[circle[i]]
    loop_cnt = (K-i-1)//len(circle)
    answer = max(answer, m_score + max(0, loop_cnt * c_score))
print(answer)