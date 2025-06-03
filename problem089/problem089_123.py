import sys
from collections import Counter
H,W,m = map(int,input().split())
h_ls = [0] * H
w_ls = [0] * W
bombers = [(0,0) for _ in range(m)]
for i in range(m):
    h,w = map(int,input().split())
    h_ls[h-1] += 1
    w_ls[w-1] += 1
    bombers[i] = (h-1,w-1)

h_max = max(h_ls)
h_counter = Counter(h_ls)
# Couter使ってみる
h_max_args = [0]*h_counter[h_max]
next_ind = 0
for i in range(H):
    if h_ls[i] == h_max:
        h_max_args[next_ind] = i
        next_ind += 1

w_max = max(w_ls)
w_counter = Counter(w_ls)
w_max_args = [0]*w_counter[w_max]
next_ind = 0
for i in range(W):
    if w_ls[i] == w_max:
        w_max_args[next_ind] = i
        next_ind += 1

bombers = set(bombers)
for h in h_max_args:
    for w in w_max_args:
        if not (h,w) in bombers:
            print(w_max+h_max)
            sys.exit()

print(w_max+h_max-1)
