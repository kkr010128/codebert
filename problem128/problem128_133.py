X, N = map(int,input().split())
p = list(map(int,input().split()))
i = 0
while True:
  if not X - i in p:
    print(X - i)
    break
  if not X + i in p:
    print(X + i)
    break
  i += 1