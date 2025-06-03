from collections import deque
k = int(input())
ans=[]
# q = deque([[1],[2],[3],[4],[5],[6],[7],[8],[9]])
q = deque([1,2,3,4,5,6,7,8,9])
while q:
  a = q.popleft()
  ans.append(a)
  if len(ans) > k:
    break
  tmp = int(str(a)[-1])
  if tmp-1 >= 0:
    q.append(10*a + tmp-1)
  q.append(10*a + tmp)
  if tmp+1 <= 9:
    q.append(10*a + tmp+1)
print(ans[k-1])