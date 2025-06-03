A, B, N = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = []
l.append(min(a) + min(b))
for _ in range(N):
  aq, bq, d = map(int, input().split())
  l.append( a[aq-1] + b[bq-1] - d )
print(min(l))