H, W, K = map(int, input().split())

choco_array = [[int(s) for s in input()] for _ in range(H)]
# print(choco_array)

ans = 100000

for i in range(1 << (H-1)):
    cut_h = 0
    cut_array = [0] * H
    for h in range(H-1):
        if i >> (h) & 1:
            cut_h += 1
        cut_array[h+1] = cut_h
    # print(cut_array)
    cut_w = 0
    now_count = [0] * (cut_h+1)
    for w in range(W):
        new_count = [0] * (cut_h+1)
        for h in range(H):
            new_count[cut_array[h]] += choco_array[h][w]
        ng_flag = 0
        # print(now_count, new_count)
        for i in range(cut_h+1):
            if new_count[i] > K:
                ng_flag = -1
                break
            if now_count[i] + new_count[i] > K:
                ng_flag = 1
                break
        if ng_flag == -1:
            cut_w = 10000
            break
        if ng_flag == 1:
            cut_w += 1
            for i in range(cut_h+1):
                now_count[i] = new_count[i]
        else:
            for i in range(cut_h+1):
                now_count[i] += new_count[i]
    ans = min(ans, cut_h+cut_w)

print(ans)
