n, p = map(int, input().split())
s = input()


def solve1(s, p):
    v = 0
    pow10 = 1
    ans = 0
    cnt = [0] * p
    cnt[0] = 1

    for i in range(n - 1, -1, -1):
        v = (pow10 * int(s[i]) + v) % p
        pow10 = (pow10 * 10) % p
        ans += cnt[v]
        cnt[v] += 1
    return ans


def solve25(s, p):
    cnt = 0
    ans = 0
    for i in range(len(s) - 1, -1, -1):
        if int(s[i]) % p == 0:
            cnt += 1
        ans += cnt
    return ans



if p in (2,5):
    print(solve25(s, p))
else:
    print(solve1(s, p))
