def main():

    N, P = map(int, input().split())
    S = input()

    if P == 2 or P == 5:
        ans = 0
        for i in range(N):
            if int(S[i]) % P == 0:
                ans += (i + 1)
        print(ans)
        exit()

    sum_rem = [0] * N
    sum_rem[0] = int(S[N - 1]) % P
    ten = 10
    for i in range(1, N):
        a = (int(S[N - 1 - i]) * ten) % P
        sum_rem[i] = (a + sum_rem[i - 1]) % P
        ten = (ten * 10) % P

    ans = 0
    count = [0] * P
    count[0] = 1
    for i in range(N):
        ans += count[sum_rem[i]]
        count[sum_rem[i]] += 1
    print(ans)


if __name__ == '__main__':
    main()
