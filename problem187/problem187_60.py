import itertools

n, x, y = map(int, input().split())

k = [0] * n

for v in itertools.combinations(list(range(1,n+1)), 2):
  k[min(abs(v[1]-v[0]),abs(x-min(v))+1+abs(y-max(v)))] += 1

for item in k[1:]:
  print(item)