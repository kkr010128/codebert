H, W, M = map(int, input().split())
h_list = [0] * H
w_list = [0] * W
target = []
for _ in range(M):
  h, w = map(int, input().split())
  h_list[h-1] += 1
  w_list[w-1] += 1
  target += [[h-1,w-1]]

h_max = max(h_list)
w_max = max(w_list)
h_max_list = set([i for i, v in enumerate(h_list) if v == h_max])
w_max_list = set([i for i, v in enumerate(w_list) if v == w_max])

place = len(h_max_list) * len(w_max_list)
candidate = 0
for h,w in target:
  if (h in h_max_list) and (w in w_max_list):
    candidate +=1

print(h_max+w_max-(place == candidate))