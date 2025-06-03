n, k, c = map(int, input().split())
plan = list(input())

a = [0] * k
b = [0] * k

idx = 0
pause = c
for i in range(n):
  pause += 1
  if plan[i]=='x':
    continue
  if pause>c and idx<k:
    a[idx] = i+1 
    idx += 1
    pause = 0
  
idx = k-1
pause = c
for i in range(n-1, -1, -1):
  pause += 1
  if plan[i]=='x':
    continue
  if pause>c:
    if idx>=0:
      b[idx] = i+1
      idx -= 1
      pause = 0
#print(a)
#print(b)

for i in range(k):
  if a[i]==b[i]:
    print(a[i])