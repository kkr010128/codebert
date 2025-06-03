n = int(input())

t = 0
for _ in range(n):
  d1,d2 = map(int, input().split())
  if d1 != d2: t = 0
  else: t += 1
    
  if t == 3:
    print("Yes")
    exit()
print("No")