def main():
    P = 2019
    S = [int(s) for s in input()]
    ans = 0
    if P == 2:
        for i, v in enumerate(S, start=1):
            if v % 2 == 0:
                ans += i
    elif P == 5:
        for i, v in enumerate(S, start=1):
            if v == 0 or v == 5:
                ans += i
    else:
        cnt = [0]*P
        d = 1
        pre = 0
        cnt[pre] += 1
        for v in S[::-1]:
            v *= d
            v += pre
            v %= P
            cnt[v] += 1
            d *= 10
            d %= P
            pre = v

        ans = sum(cnt[i]*(cnt[i]-1)//2 for i in range(P))

    print(ans)


if __name__ == '__main__':
    main()
