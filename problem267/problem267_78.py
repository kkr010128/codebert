def main():
    N = int(input())
    S = input()
    ans = 0
    # password = set()

    # for i in range(N - 2):
    #     for j in range(i + 1, N - 1):
    #         for k in range(10):
    #             if str(k) in S[j + 1:]:
    #                 password.add(S[i] + S[j] + str(k))

    for i in range(10):
        for j in range(10):
            for k in range(10):
                i_index = S.find(str(i))
                j_index = S.find(str(j), i_index + 1)
                k_index = S.find(str(k), j_index + 1)
                if i_index != -1 and j_index != -1 and k_index != -1:
                    ans += 1

    print(ans)


if __name__ == "__main__":
    main()
