from collections import deque
 
K = int(input())
 
count = 0
Q = deque([1,2,3,4,5,6,7,8,9])
while count != K:
  a = Q.popleft()
  b = a%10
  if b != 0:
    Q.append(a*10 + b - 1)
  Q.append(a*10 + b)
  if b != 9:
    Q.append(a*10 + b + 1)
  count += 1
  #print(Q)
print(a)