import itertools

n = int(input())
d = list(map(int,input().split()))
ans = 0
for v in itertools.combinations(d, 2):
  ans += v[0]*v[1]
print(ans)