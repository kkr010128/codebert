L, R, d = map(int, input().split())

count = 0

for i in range(101):
  if d * i >= L and d * i <= R:
    count += 1
  if d * i > R:
    break
    
print(count)