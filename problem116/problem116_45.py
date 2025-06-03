def resolve():
    S = input()
    T = input()
    cnt = 0
    for i in range(len(S)):
        s = S[i]
        t = T[i]
        if s != t:
            cnt += 1
    print(cnt)
resolve()