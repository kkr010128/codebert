
def resolve():
    l, P = map(int, input().split())
    S = input()

    ans = 0
    # 10^r: 2^r * 5^r の為、10と同じ素数
    if P == 2 or P == 5:
        for i, s in enumerate(S):
            if int(s) % P == 0:
                ans += i + 1
        return print(ans)

    cnts = [0] * P
    cnts[0] = 1
    num, d = 0, 1
    for s in S[::-1]:
        s = int(s)
        num = (num + (s * d)) % P
        d = (10 * d) % P
        cnts[num] += 1

    for cnt in cnts:
        ans += cnt * (cnt - 1) // 2
    print(ans)


if __name__ == "__main__":
    resolve()