N = int(input())
ans = 0

for a in range(1,N//2 +1):
  b = N - a
  if a == b:
    continue
  else:
    ans += 1
    
print(ans)