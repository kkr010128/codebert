def resolve():
    N = int(input())
    S = str(input())
    ans = 0

    for pos in range(N - 2):
        if S[pos:(pos + 3)] == 'ABC':
            ans += 1
    print(ans)
    return


resolve()