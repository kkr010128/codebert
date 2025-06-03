from collections import deque
X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse=True)
q.sort(reverse=True)
r = sorted(r, reverse=True)

ans_p = deque(p[:X])
ans_q = deque(q[:Y])
ans_r = deque(r)

while (ans_p[-1]<ans_r[0]) or (ans_q[-1]<ans_r[0]):
  if ans_p[-1] <= ans_q[-1]:
    ans_p.pop()
    ans_p.appendleft(ans_r[0])
    ans_r.popleft()
  else:
    ans_q.pop()
    ans_q.appendleft(ans_r[0])
    ans_r.popleft()
  if not ans_r:
    break;
    
ans = sum(ans_p) + sum(ans_q)
print(ans)