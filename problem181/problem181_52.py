from collections import deque
K = int(input())
q = deque([1,2,3,4,5,6,7,8,9])

for i in range(K):
  num = q.popleft()
  if num%10 != 0:
    q.append(num*10+num%10-1)
  q.append(num*10+num%10)
  if num%10 != 9:
    q.append(num*10+num%10+1)

print(num)