A, B, M = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

res = min(a) + min(b)
for _ in range(M):
  x, y, c = map(int, input().split())
  discounted_v = a[x-1] + b[y-1] - c
  if discounted_v < res: res = discounted_v
  
print(res)
  
           


