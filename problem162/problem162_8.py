n, m = map(int, input().split())

if n % 2 or m < n//4:
  for i in range(m):
    print(i+1, n-i)
else:
  for i in range(n//4):
    print(i+1, n-i)
  for i in range(n//4, m):
    print(i+1, n-i-1)