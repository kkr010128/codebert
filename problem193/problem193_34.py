
def main():
    H,W,K = list(map(int, input().split()))
    S = ['' for i in range(H)]
    for i in range(H):
        S[i] = input()

    ans = H*W

    for i in range(0,1<<(H-1)):
        g = 0
        id = [0 for j in range(H)]
        for j in range(0,H):
            id[j] = g
            if i>>j&1 == 1:
                g += 1
        
        g_cnt = [0 for j in range(g+1)]
        c_ans = g
        j = 0
        div_w = 0
        while j < W:
            for k in range(0, H):
                if S[k][j] == '1':
                    g_cnt[id[k]] += 1
            for k in range(0,g+1):
                if g_cnt[k] > K:
                    c_ans += 1
                    g_cnt = [0 for j in range(g+1)]
                    if div_w == j:
                        c_ans += H*W
                        break
                    j -= 1
                    div_w = j
                    break
            j += 1
            if c_ans > ans:
                break
        
        ans = min(ans, c_ans)

    
    print(ans)


main()