H, W, M = map(int, input().split())

h_cnt = [0] * H
w_cnt = [0] * W
hw = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
for h, w in hw:
    h_cnt[h] += 1
    w_cnt[w] += 1

max_h = max(h_cnt)
max_w = max(w_cnt)
hs = [i for i in range(H) if h_cnt[i]==max_h]
ws = [i for i in range(W) if w_cnt[i]==max_w]

ans = max_h+max_w-1
hw = set(hw)
for h in hs:
    for w in ws:
        if (h, w) not in hw:
            print(max_h+max_w)
            exit()
print(max_h+max_w-1)

