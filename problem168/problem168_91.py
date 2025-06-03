n, m = map(int , input().split())
a = [int(num) for num in input().split()]
st = sum(a)

if (n >= st):
  print(n-st)
else :
  print(-1)
