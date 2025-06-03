H, A = map(int, input().split())

res = H // A
if H % A:
  res += 1
  
print(res)