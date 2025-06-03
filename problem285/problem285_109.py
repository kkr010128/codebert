def resolve():
    S = list(input())
    ans = [0 for _ in range(len(S) + 1)]
    cnt = 0
    for i in range(len(S)):
        if S[i] == "<":
            cnt += 1
            ans[i + 1] = max(cnt, ans[i + 1])
        else:
            cnt = 0
    cnt = 0
    for i in range(len(S), 0, -1):
        if S[i - 1] == ">":
            cnt += 1
            ans[i - 1] = max(cnt, ans[i - 1])
        else:
            cnt = 0
    print(sum(ans))


resolve()
