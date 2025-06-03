def main():
    N, K = map(int, input().split())
    P = list(map(lambda x: int(x)-1, input().split()))
    C = list(map(int, input().split()))
    loop = [0] * N
    loopsum = [0] * N
    for i in range(N):
        if loop[i] > 0:
            continue
        cnt = 0
        cur = i
        visited = set()
        score = 0
        while cur not in visited:
            visited.add(cur)
            cnt += 1
            cur = P[cur]
            score += C[cur]
        for v in visited:
            loop[v] = cnt
            loopsum[v] = score
    ans = max(C)
    for i in range(N):
        if loopsum[i] >= 0 and loop[i] <= K:
            score = loopsum[i] * (K // loop[i] - 1)
            limit = K % loop[i] + loop[i]
        else:
            score = 0
            limit = min(loop[i], K)
        cur = i
        for _ in range(limit):
            cur = P[cur]
            score += C[cur]
            ans = max(ans, score)
    print(ans)


if __name__ == "__main__":
    main()
