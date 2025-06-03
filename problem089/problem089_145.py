H, W, M = map(int, input().split())
bomb = []
h_sum = [0]*W
w_sum = [0]*H
for _ in range(M):
    h, w = map(int, input().split())
    bomb.append((h,w))
    h_sum[w-1] += 1
    w_sum[h-1] += 1
max_h = max(h_sum)
max_w = max(w_sum)
target_cnt = h_sum.count(max_h)*w_sum.count(max_w)
for h, w in bomb:
    if h_sum[w-1] == max_h and w_sum[h-1] == max_w:
        target_cnt -= 1
if target_cnt == 0:
    print(max_h+max_w-1)
else:
    print(max_h+max_w)