def main():
    S = input()
    T = input()
    l_s = len(S)
    l_t = len(T)

    cnt_list = []
    for i in range(l_s - l_t + 1):
        cnt = 0
        S_ = S[i: i+l_t]
        for j in range(l_t):
            if S_[j] != T[j]:
                cnt += 1
        cnt_list.append(cnt)

    ans = min(cnt_list)
    print(ans)
    return


if __name__ == '__main__':
    main()
