h,w,m=map(int,input().split())
bomb=[list(map(int,input().split())) for i in range(m)]

num_h = [0] * (h+1)
num_w = [0] * (w+1)
bomb_set = set()
for hi,wi in bomb:
  num_h[hi] += 1
  num_w[wi] += 1
  bomb_set.add((hi,wi))
  
max_h = max(num_h)
max_w = max(num_w)
max_hs = [k for k,v in enumerate(num_h) if v == max_h]
max_ws = [k for k,v in enumerate(num_w) if v == max_w]

result = max_h + max_w
for i in max_hs:
  for j in max_ws:
    if (i,j) not in bomb_set:
      print(result)
      exit(0)
print(result-1)
