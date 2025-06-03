from itertools import groupby


def main():

    S = input()
    K = int(input())
    a = [len(tuple(s)) for _, s in groupby(S)]
    ans = 0

    if S[0] == S[-1] and K > 1:
        if len(a) == 1:
            ans = a[0] * K // 2
        else:
            ans = a[0] // 2 + a[-1] // 2 + (a[0] + a[-1]) // 2 * (K - 1)
            ans += sum(n // 2 for n in a[1:-1]) * K

    else:
        ans += sum(n // 2 for n in a) * K

    print(ans)


if __name__ == "__main__":
    main()