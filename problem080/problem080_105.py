N = int(input())

a = [0 for i in range(N)]
b = [0 for i in range(N)]

for i in range(N):
  x, y = list(map(int, input().split()))
  a[i] = x + y
  b[i] = x - y

a = sorted(a)
b = sorted(b)
print(max(a[N-1]-a[0], b[N-1]-b[0]))