H, W, M = map(int, input().split())
hw = set()
cnt_h, cnt_w = [0] * H, [0] * W
for i in range(M):
    x, y = map(int, input().split())
    hw.add((x - 1, y - 1))
    cnt_h[x - 1] += 1
    cnt_w[y - 1] += 1

max_h, max_w = max(cnt_h), max(cnt_w)

h_list = [h for h in range(H) if cnt_h[h] == max_h]
w_list = [w for w in range(W) if cnt_w[w] == max_w]

res = max_h + max_w - 1
for h in h_list:
    for w in w_list:
        if (h, w) not in hw:
            print(res + 1)
            exit()
print(res)
