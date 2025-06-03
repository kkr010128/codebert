n , x , t = map(int, input().split())
c = 0
for i in range(n):
  n = n - x
  c = c + t
  if n <= 0:
    print(c)
    break