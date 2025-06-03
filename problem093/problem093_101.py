def solve_loop(loop, K):
    S = sum(loop)
    L = len(loop)
    if S < 0:
        acc = 0
        K = min(K, L)
        minL = 1
    elif K//L >= 2:
        acc = S * (K//L - 1)
        K = K - L * (K//L - 1)
        minL = 0
    else:
        acc = 0
        minL = 1

    ans = -10 ** 9 - 1
    for i in range(L):
        #print(loop[i:] + loop[:i], "acc=", acc, "min=", minL, "max=", K)
        tmp = 0
        if minL:
            tmp = loop[i]

        for l in range(minL, K):
            ans = max(tmp, ans)
            tmp += loop[(i+l) % L]
            #print(tmp)
            #print(i, l, tmp)
        ans = max(tmp, ans)

    #print(loop, ans, acc)
    return acc + ans
    if K >= L:
        return max(acc, acc + ans)
    else:
        return ans

def solve():
    N, K = map(int, input().split())
    P = list(map(lambda n: int(n)-1, input().split())) # 0-based index
    C = list(map(int, input().split()))

    flag = [False] * N
    ans = -10**9-1  # worst case is -10**9
    for i in range(N):
        if flag[i]:
            continue
        loop = []
        j = P[i]
        for _ in range(N):
            if flag[j]: # loop end
                break
            flag[j] = True
            loop += [C[j]]
            j = P[j]
        ans = max(ans, solve_loop(loop, K))
    print(ans)

solve()