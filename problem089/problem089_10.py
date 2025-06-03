import sys
 
h, w, m = map(int, input().split(' '))
H = [0 for _ in range(h+1)]
W = [0 for _ in range(w+1)]
bomb = set()
for m in range(m):
  i, j = map(int, input().split(' '))
  bomb.add((i, j))
  H[i] += 1
  W[j] += 1
  
max_h = max(H)
max_w = max(W)
target_h = [i for i, v in enumerate(H) if v == max_h]
target_w = [i for i, v in enumerate(W) if v == max_w]
 
for m in target_h:
  for n in target_w:
    if (m, n) not in bomb:
      print(max_h + max_w)
      sys.exit()
	
print(max_h + max_w - 1)