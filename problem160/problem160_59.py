import itertools
N,M,Q = map(int,input().split())
cc = [list(map(int,input().split())) for i in range(Q)]
a = [i for i in range(1,M+1)]
max_count = -float('inf')
for i in itertools.combinations_with_replacement(a,N):
  count = 0
  for j in cc:
    if i[j[1]-1] - i[j[0]-1] == j[2]:
      count += j[3]
  max_count = max(max_count,count)
print(max_count)