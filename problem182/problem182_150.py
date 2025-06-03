def main():
    N, K, C = map(int, input().split())
    S = input()
    L, R = [-C], [N + C]
    i, k = 0, 0
    while i < N and k < K:
        if S[i] == 'o':
            L.append(i)
            k += 1
            i += C
        i += 1
    L.append(N)
    i, k = N - 1, 0
    while 0 <= i and k < K:
        if S[i] == 'o':
            R.append(i)
            k += 1
            i -= C
        i -= 1
    R.append(N)

    l = 0
    for i, s in enumerate(S):
        if s == 'x':
            continue
        r = K - l
        if R[r] <= i or R[r] - L[l] < C:
            print(i + 1)
        if L[l + 1] == i:
            l += 1


main()
