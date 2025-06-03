A, B = map(int, input().split())

ans = 0
for i in range(B):
  ans += A
  if ans%B == 0:
    break
    
print(ans)