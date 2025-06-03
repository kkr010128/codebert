def resolve():
    N = int(input())
    S = str(input())
    cnt = 0

    for i in range(1000):
        c = [int(i / 100), int(i / 10) % 10, int(i % 10)]
        f = 0

        for j in range(N):
            if S[j] == ('0' + str(c[f])) or S[j] == str(c[f]):
                f += 1
            if f == 3:
                break

        if f == 3:
            cnt += 1
    print(cnt)
    return

resolve()