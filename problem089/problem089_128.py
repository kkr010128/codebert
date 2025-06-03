def main():
    H,W,M = map(int,input().split())
    s = []
    h_cnt = [0 for i in range(H)]
    w_cnt = [0 for i in range(W)]
    for i in range(M):
        h,w = map(int,input().split())
        s.append([h-1,w-1])
        h_cnt[h-1] += 1
        w_cnt[w-1] += 1
    h_m,w_m = max(h_cnt), max(w_cnt)
    h_mp,w_mp = [],[]
    for i in range(H):
        if h_cnt[i] == h_m:
            h_mp.append(i)
    for i in range(W):
        if w_cnt[i] == w_m:
            w_mp.append(i)
    f = 0
    for i in range(M):
        if h_cnt[s[i][0]] == h_m and w_cnt[s[i][1]] == w_m:
            f += 1
    if len(w_mp)*len(h_mp)-f<1:
        print(h_m+w_m-1)
    else:
        print(h_m+w_m)

if __name__ == "__main__":
    main()
