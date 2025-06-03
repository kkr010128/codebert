def main():
    from itertools import product

    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]
    S_T = [[int(s[w]) for s in S] for w in range(W)]
    sumS = sum(map(sum, S_T))
    ans = (H - 1) * (W - 1)

    if sumS <= K:
        print(0)
    else:
        for i in product([True, False], repeat=H-1):
            cnt = sum(i)
            if cnt >= ans:
                continue
            M = [[0]]
            for j, k in enumerate(i):
                if k:
                    M.append([])
                M[-1].append(j+1)
            A = [0] * len(M)
            for s_t in S_T:
                for l, m in enumerate(M):
                    A[l] += sum(s_t[i] for i in m)
                if any(a > K for a in A):
                    cnt += 1
                    if cnt >= ans:
                        break
                    A = [sum(s_t[i] for i in m) for m in M]
                    if any(a > K for a in A):
                        cnt = ans + 1
                        break
            ans = min(cnt, ans)
        print(ans)

if __name__ == '__main__':
    main()