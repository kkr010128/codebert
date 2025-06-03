import itertools

h, w, k = map(int, input().split())
c = [[x for x in input()] for i in range(h)]

ans = 0

for hi in range(2**h):
  for wi in range(2**w):
    c_cp = [[n for n in i] for i in c]
    
    for hj in range(h):
      if (hi & (1<<hj)) != 0:
        c_cp[hj] = ['R' for n in c_cp[hj]]
    
    for wj in range(w):
      if (wi & (1<<wj)) != 0:
        for hk in range(h):
          c_cp[hk][wj] = 'R'
    
    cnt = list(itertools.chain.from_iterable(c_cp)).count('#')
    
    if cnt == k:
      ans += 1

print(ans)