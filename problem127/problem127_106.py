x, y = map(int, input().split())
lst = []
ans = 'No'

for i in range(x):
  lst.append(2)

for i in range(x):
  if sum(lst) == y:
    ans = 'Yes'
    break
  lst[i] = 4
    
if sum(lst) == y:
    ans = 'Yes'
    
print(ans)