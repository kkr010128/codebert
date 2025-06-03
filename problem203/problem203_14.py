A, B = map(int, input().split())

ans1 = 0
ans2 = 0

for i in range(10000):
  ans1 = int(i * 0.08)
  ans2 = int(i * 0.10)
  
  if (ans1) == A and int(ans2) == B:
    print(i)
    exit()
    
print(-1)
