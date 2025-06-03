ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

a,b = nm()

if a<10 and b<10:
  print(a*b)
  exit()
print(-1)