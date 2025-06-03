def solve():
    H,W,M = map(int,input().split())
    h_counter = [0] * H
    w_counter = [0] * W

    opponents = []
    for _ in range(M):
        h, w = map(lambda x:int(x)-1, input().split())
        h_counter[h] += 1
        w_counter[w] += 1
        opponents.append((h,w))
    
    h_max = max(h_counter)
    w_max = max(w_counter)

    h_max_area_cnt = 0
    h_max_area_nums = set()
    for h in range(H):
        if h_counter[h] == h_max:
            h_max_area_nums.add(h)
            h_max_area_cnt += 1

    w_max_area_cnt = 0
    w_max_area_nums = set()
    for w in range(W):
        if w_counter[w] == w_max:
            w_max_area_nums.add(w)
            w_max_area_cnt += 1

    max_area_cnt = h_max_area_cnt * w_max_area_cnt

    opponent_in_max_area = 0
    for h,w in opponents:
        if h in h_max_area_nums and w in w_max_area_nums:
            opponent_in_max_area += 1

    if max_area_cnt > opponent_in_max_area:
        print(h_max + w_max)
    else:
        print(h_max + w_max - 1)

if __name__ == '__main__':
    solve()
