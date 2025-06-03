from collections import defaultdict


def main():
    N, P = map(int, input().split())
    S = input()
    ans = 0
    if P in [2, 5]:
        for i, d in enumerate(S[::-1]):
            if int(d) % P == 0:
                ans += N - i
    else:
        total = defaultdict(int)
        total[0] = 1
        cur = 0
        for i, d in enumerate(S[::-1]):
            d = int(d) % P
            prev = cur
            cur = (prev + pow(10, i, P) * d) % P
            ans += total[cur]
            total[cur] += 1
    print(ans)


if __name__ == "__main__":
    main()
