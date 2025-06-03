import sys

input = sys.stdin.readline

def main():
    H, W, K = map(int, input().split())
    stro = []; remain = K
    start = H; end = 0
    idx = 0
    ans = []
    for i in range(H):
        tmp = list(input()[:-1])
        cnt = 0
        for j in tmp:
            cnt += j == '#'
        stro.append(cnt)
        remain -= cnt
        if cnt > 0:
            start = min(start, i)
            end = max(end, i)
        if cnt == 1:
            idx += 1
            ans.append([idx]*W)
        elif cnt >= 2:
            idx += 1
            cnttmp = 0
            anstmp = []
            for j in tmp:
                cnttmp += j=='#'
                idx += (cnttmp != 1 and j == '#' and cnt > 0)
                cnt -= (j == '#' and cnt > 0)*1
                anstmp.append(idx)
            ans.append(anstmp)
        else:
            if remain == K:
                continue
            anstmp = ans[-1].copy()
            ans.append(anstmp)
    
    for _ in range(start):
        print(*ans[0])
    for i in range(len(ans)):
        print(*ans[i])
        
if __name__ == "__main__":
    main()
