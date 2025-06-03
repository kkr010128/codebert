import sys

h,w,m = map(int, sys.stdin.readline().split())
num_in_h = [0] * h
num_in_w = [0] * w
targets = set()
for _ in range(m):
    t_h, t_w = map(lambda x: int(x)-1, sys.stdin.readline().split())
    num_in_h[t_h] += 1
    num_in_w[t_w] += 1
    targets.add((t_h, t_w))

max_h = max(num_in_h)
max_w = max(num_in_w)
max_h_set = set([i for i, v in enumerate(num_in_h) if v == max_h])
max_w_set = set([i for i, v in enumerate(num_in_w) if v == max_w])
ans = max_h + max_w - 1

flag = False
for i in max_h_set:
    for j in max_w_set:
        if (i, j) not in targets:
            flag = True
            break
    if flag: break

print(ans+1 if flag else ans)
